from sqlalchemy import Column, Integer, String, Enum, text
from database_config import Base
from enums.roles_enums import Role

class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  username = Column(String, unique=True, index=True)
  password = Column(String)
  role = Column(Enum(Role), default=Role.customer)
  location = Column(String, server_default=text("Lagos, Nigeria"), nullable=False)