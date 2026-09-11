from sqlalchemy.orm import Session
from models import Product
import schemas

def get_product(db: Session, id: int):
  return db.query(Product).filter(Product.id == id).first()

def get_products(db: Session):
  return db.query(Product).all()

def create_product(db: Session, name: str, description: str, price: float, stock: int, category: str, is_available: bool):
  new_product = Product(name=name, description=description, price=price, stock=stock, category=category, is_available=is_available)
  db.add(new_product)
  db.commit()
  db.refresh(new_product)
  return new_product

def update_product(db: Session, id: int, product_update: schemas.ProductUpdate):
  db_product = db.query(Product).filter(Product.id == id).first()
  if not db_product:
    return None

  update_prod = product_update.model_dump(exclude_unset=True)

  for key, value in update_prod.items():
    setattr(db_product, key, value)

  db.commit()
  db.refresh(db_product)

def delete_product(db: Session, id: int) -> bool:
  db_product = db.query(Product).filter(Product.id == id).first()

  if not db_product:
    return False

  db.delete(db_product)
  db.commit()
  return True