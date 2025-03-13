from sqlalchemy.orm import Session
from database_config import get_db
from fastapi import Depends
from dtos.user_dto import UserDto
from models.user_model import User


async def create_user(body:UserDto, db: Session = Depends(get_db)):
  new_user = User(email=body.email, username=body.username)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user