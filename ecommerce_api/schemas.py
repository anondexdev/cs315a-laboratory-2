from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  stock: int
  category: str
  is_available: bool

class ProductCreate(ProductBase):
  pass

class ProductUpdate(ProductBase):
  name: Optional[str] = None
  description: Optional[str] = None
  price: Optional[float] = None
  stock: Optional[int] = None
  category: Optional[str] = None
  is_available: Optional[bool] = None

class ProductResponse(ProductBase):
  id: int

  model_config = ConfigDict(from_attributes=True)