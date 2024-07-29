import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Get database URL from environment variable or use a default
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:thefallingsky195@localhost/ads_db")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()

def get_db():
    """
    Generator function to get database session.
    Usage: 
    db = next(get_db())
    try:
        # use db for database operations
    finally:
        db.close()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()