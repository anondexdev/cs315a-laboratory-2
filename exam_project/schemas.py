from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class CategoryBase(BaseModel):
  name: str
  description: str

class CategoryCreate(CategoryBase):
  pass

class CategoryResponse(CategoryBase):
  id: int
  category_id: int

  model_config = ConfigDict(from_attributes=True)

#-----------------------------------------------

class BookBase(BaseModel):
  title: str
  isbn: str
  publication_year: int
  stock_quantity: int

class BookCreate(BookBase):
  pass

class BookResponse(BookBase):
  id: int
  book: List[CategoryResponse] = []
  model_config = ConfigDict(from_attributes=True)