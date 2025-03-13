from sqlalchemy.orm import Session
from database_config import get_db
from fastapi import Depends, HTTPException
from dtos.user_dto import UserDto
from models.user_model import User


async def create_user(body:UserDto, db: Session = Depends(get_db)):
  new_user = User(email=body.email, username=body.username)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user


async def get_users(db:  Session = Depends(get_db)):
  return db.query(User).all()

async def get_user_by_id(user_id: int, db: Session):
  user =  db.query(User).filter(User.id == user_id).first()
  if user is None:
    raise HTTPException(status_code=404, detail="User not found")
  return user