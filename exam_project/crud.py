from sqlalchemy.orm import Session
from models import Category, Books
import schemas

#----------Categories

def create_category(db: Session, name: str, description: str):
  new_category = Category(name=name, description=description)
  db.add(new_category)
  db.commit()
  db.refresh(new_category)
  return new_category

def get_categories(db: Session):
  return db.query(Category).all()

#--------------Books

def create_book(db: Session, title: str, isbn: str, publication_year: int, stock_quantity: int, category_id: int):
  new_book = Books(title=title, isbn=isbn, publication_year=publication_year, stock_quantity=stock_quantity, category_id=int)
  db.add(new_book)
  db.commit()
  db.refresh(new_book)
  return new_book

