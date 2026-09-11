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

@app.post("/products/", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
def create_item_route(name: str, description: str, price: float, stock: int, category: str, is_available: bool, db: Session = Depends(get_db)):
  return crud.create_product(db=db, name=name, description=description, price=price, stock=stock, category=category, is_available=is_available)

@app.get("/products", response_model=schemas.ProductResponse, status_code=status.HTTP_200_OK)
def get_products(skip: int=0, limit: int=10  )

@app.get("/products/{product_id}", response_model=schemas.ProductResponse, status_code=status.HTTP_200_OK)
def get 
