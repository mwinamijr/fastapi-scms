from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Database URL from environment settings
DATABASE_URL = settings.DATABASE_URL

# SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# SessionLocal for creating database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base: DeclarativeMeta = declarative_base()


# Dependancy for databse session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
