from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# use sqlite for local development
SQLALCHEMY_DATABASE_URL = "sqlite:///ecommerce.db"

engine = create_engine()

SessionLocal = sessionmaker(autocommit=False, autoflush=Flase, bind=engine)

Base = declarative_base()
