from unicodedata import category
from pygments.unistring import categories
from typing import List
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine, Model, get_db
import models
import schemas

Model.metadata.create_all(bind=engine)

app=FastAPI(title="Library_Manager_System")

#Categories-----------

@app.post("/categories/", response_model=schemas.CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(name: schemas.CategoryCreate, db: Session = Depends(get_db)):
  existing = db.query(models.Category).filter(models.Category.name == category.name).first()
  if existing:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail=f'Category already exists',
    )
  new_category = models.Category(name=category.name)
  db.add(new_category)
  db.commit()
  db.refresh(new_category)
  return new_category