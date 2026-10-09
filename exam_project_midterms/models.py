from typing import List
from sqlalchemy import ForeignKey, String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Model

class Category(Model):
  __tablename__ = "categories"

  id: Mapped[int] = mapped_column(primary_key=True, index=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False, unique= True)

  books: Mapped[List["Book"]] = relationship(back_populates="category")

class Book(Model):
  __tablename__ = "books"

  id: Mapped[int] = mapped_column(primary_key=True, index=True)
  title: Mapped[str] = mapped_column(String(100), nullable=False)
  isbn: Mapped[str] = mapped_column(String(13), unique=True, nullable=False)
  publication_year: Mapped[int] = mapped_column(index=True)
  stock_quantity: Mapped[int] = mapped_column(index=True, default=1)

  category_id: Mapped["Category"] = relationship(back_populates="books")
  