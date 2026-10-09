from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(
  DATABASE_URL,
  connect_args={"check_same_threat": False},
  echo=True
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Model(DeclarativeBase):
  pass

def get_db():
  db = Session()
  try:
    yield db
  finally:
    db.close()