from sqlalchemy import Column, Integer, String, Enum
from database_config import Base
from enums.roles_enums import Role
from sqlalchemy.orm import relationship, Mapped
from .article_model import Article


#* just realized that "Column" class the legacy version of creating columns with sqlalchemy. 
# The "mapped_column" class is the new version of creating columns with sqlalchemy. 
# The "mapped_column" class is a more modern and flexible way to define columns in SQLAlchemy models. 
# It allows for better type hinting and integration with type checkers, making it easier to work with SQLAlchemy in a type-safe manner.
# The "Column" class is still available for backward compatibility, but it's recommended to use "mapped_column" for new code.
class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  username = Column(String, unique=True, index=True)
  password = Column(String)
  role = Column(Enum(Role), default=Role.customer)
  location = Column(String, default="Lagos, Nigeria")

  articles = relationship("Article", cascade="all, delete") # one to many relationship with article model