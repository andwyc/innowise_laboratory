from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Indicate an address of database
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# Create Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base
Base = declarative_base()