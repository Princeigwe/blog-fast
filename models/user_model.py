from sqlalchemy import Column, Integer, String, Enum
from database_config import Base
from enums.roles_enums import Role

class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  username = Column(String, unique=True, index=True)
  password = Column(String)
  role = Column(Enum(Role), default=Role.customer)