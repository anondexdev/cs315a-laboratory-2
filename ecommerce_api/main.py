from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine, Model, get_db
import models
import schemas
import crud, database

Model.metadata.create_all(bind=engine)

app=FastAPI(title="Ecommerce_API")

@app.post("/products/", response_model=schemas.ProductCreate, status_code=status.HTTP_201_CREATED)
def create_item_route(name: str, description: str, price: float, stock: int, category: str, is_available: bool, db: Session = Depends(get_db)):
  return crud.create_product(db=db, name=name, description=description, price=price, stock=stock, category=category, is_available=is_available)

@app.get("/products", response_model=schemas.ProductResponse, status_code=status.HTTP_200_OK)
def get_products(skip: int=0, limit: int=10,db: Session = Depends(get_db)):
  return crud.get_products(db=db)

@app.get("/products/{product_id}", response_model=schemas.ProductResponse, status_code=status.HTTP_200_OK)
def get_product(id: int, db: Session = Depends(get_db)):
  return crud.get_product(db=db, id=id)

@app.put("/products/{product_id}", response_model=schemas.ProductUpdate, status_code=status.HTTP_200_OK)
def update_product(id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
  updated_prd = crud.update_product(db=db,id=id, product_update=product)
  if updated_prd is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail=f"Item with ID {id} not found"
    )
    return updated_prd

@app.patch("/products/{product_id}/stock", response_model=schemas.ProductUpdate, status_code=status.HTTP_200_OK)
def stock_quantity(quantity: int):
  updated_quantity = quantity

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(db:Session=Depends(get_db)):
  return crud.delete_product
  
