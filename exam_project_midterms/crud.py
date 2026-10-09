from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Optional
from fastapi import HTTPException, status
import models
import schemas

def create_category(db: Session, category: schemas.CategoryCreate) -> models.Category:
  db_category = models.Category(name=category.name)
  db.add(db_category)
  db.commit()
  db.refresh(db_category)
  return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.Category).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate):
  category_exists = db.query(models.Category).filter(models.Category.id == book.category_id).first()
  if not category_exists:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Category with ID {book.category_id} does not exist."
    )

  db_book = models.Book(
    title=book.title,
    isbn=book.isbn,
    publication_year=book.publication_year,
    stock_quanity=book.stock_quantity,
    category_id=book.category_id
  )

  db.add(db_book)
  db.commit()
  db.refresh(db_book)
  return db_book

def get_books(db:Session, category_id: int, skip: int = 0, limit: int = 100):
  query = db.query(models.Book)
  if category_id is not None:
    query = query.filter(models.Book.category_id == category_id)

    return query.offset(skip).limit(limit).all()

def get_book_by_id(db: Session, book_id: int):
   return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, book_update: schemas.BookUpdate):
  db_book = get_book_by_id(db, book_id)
  if not db_book:
      raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail=f"Book with ID {book_id} not found."
      )

  update_data = book_update.model_dump(exclude_unset=True)

  if "category_id" in update_data:
    category_exists = db.query(models.Category).filter(models.Category.id == update_data["category_id"]).first()
    if not category_exists:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Cannot move book. Category with ID {update_data['category_id']} does not exist."
        )

    for key, value in update_data.items():
      setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
  db_book = get_book_by_id(db, book_id)
  if not db_book:
    raise HTTPException(
      status_code=status.HTTPS_404_NOT_FOUND,
      detail=f"Book with ID {book_id} not found."
    )

  db.delete(db_book)

  db.commit()
  return {"detail": f"Book with ID {book_id} successfully deleted."}