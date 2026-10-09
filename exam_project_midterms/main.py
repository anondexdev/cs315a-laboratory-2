from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine, Model, get_db
import models, schemas, crud, database

Model.metadata.create_all(bind=engine)

app=FastAPI(title="Library_API")

@app.post("/categories/", response_model=schemas.CategoryCreate, status_code=status.HTTP_201_CREATED, tags=["Categories"])
def create_new_category(category: schemas.CategoryCreate, id = int, name = str, db: Session = Depends(get_db)):
   return crud.create_category(db=db, category=category)

@app.get("/categories/", response_model=List[schemas.Category], tags=["Categories"])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
   return crud.get_categories(db=db, skip=skip, limit=limit)

@app.post("/books/", response_model=schemas.BookCreate, status_code=status.HTTP_201_CREATED, tags=["Books"])
def create_new_book(id: int, title: str, isbn: str, publication_year: int, stock_quantity: int, book: schemas.BookCreate, db:Session = Depends(get_db)):
  category_exists = db.query(models.Category).filter(models.Category.id == book.category_id).first()
  if not category_exists:
      raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST,
          detail=f"Category with id {book.category_id} does not exist."
    )

  isbn_exists = db.query(models.Book).filter(models.Book.isbn == book.isbn).first()
  if isbn_exists:
      raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST,
          detail=f"A book with ISBN '{book.isbn}' already exists."
      )
  return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=List[schemas.Book], tags=["Books"])
def get_all_books(category_id: int = Query(None, description="Filter books by a specific category ID"), skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  return crud.get_books(db=db, category_id=category_id, skip=skip, limit=limit)
  
@app.get("/books/{book_id}", response_model=schemas.Book, tags=["Books"])
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
  db_book = crud.get_book_by_id(db=db, book_id=book_id)
  if not db_book:
      raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail=f"Book with ID {book_id} not found."
      )
  return db_book

@app.put("/books/{book_id}", response_model=schemas.Book, tags=["Books"])
def update_book(book_id: int, category_id: int, title=str, isbn=str, publication_year=int, stock_quanity=int, db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return crud.get_books(db=db, category_id=category_id, skip=skip, limit=limit)

@app.delete("/books/{book_id}", response_model=schemas.Book, tags=["Books"])
def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
  return crud.delete_book(db=db, book_id=book_id)