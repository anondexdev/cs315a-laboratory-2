from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

class BookBase(BaseModel):
  title: str = Field(..., max_length=100, description="The title of the book")
  isbn: str
  publication_year: int
  stock_quantity: int = Field(default=1)
  category_id: int

class BookCreate(BookBase):
  pass

class BookUpdate(BookBase):
  title: Optional[str] = None
  isbn: Optional[str] = None
  publication_year: Optional[int] = Field(None, ge=0)
  stock_quantity: Optional[int] = Field(None, ge=0)
  category_id: Optional[int] = None

class Book(BookBase):
  id: int
  class Config:
    from_attributes = True

class CategoryBase(BaseModel):
  name: str = Field(..., max_length=50, description="The unique name of the category")
  class Config:
    from_attributes = True

class CategoryCreate(CategoryBase):
  pass

class Category(CategoryBase):
  id: int
  class Config:
    from_attributes = True

