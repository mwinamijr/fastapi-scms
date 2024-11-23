from app.database import Base


# All models will inherit from this
class BaseModel(Base):
    __abstract__ = True
