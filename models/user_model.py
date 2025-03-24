from sqlalchemy import Column, Integer, String
from database_config import Base

class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  username = Column(String, unique=True, index=True)
  password = Column(String)