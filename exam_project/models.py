from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Model

class Category(Model):
  __tablename__ = "categories"

  id: Mapped[int] = mapped_column(primary_key=True, index=True)
  name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
  description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

  book: Mapped[List["Books"]] = relationship(back_populates="id")

class Books(Model):
  __tablename__ = "book"

  id: Mapped[int] = mapped_column(primary_key=True, index=True)
  title: Mapped[str] = mapped_column(String(100), nullable=False)
  isbn: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
  publication_year: Mapped[int] = mapped_column(index=True)
  stock_quantity: Mapped[int] = mapped_column(index=True, default=1)

  category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))

  