from sqlalchemy.orm import Session
from database_config import get_db
from fastapi import Depends, HTTPException, status
from dtos.user_dto import UserDto
from models.user_model import User
from email_validator import validate_email, EmailNotValidError
from utils.jwt_encode_decode import decode_access_token


async def create_user(body:UserDto, db: Session = Depends(get_db)):
  # fetching existing user with email and username
  existing_user_with_email = db.query(User).filter(User.email==body.email).first()
  existing_user_with_username = db.query(User).filter(User.username==body.username).first()
  if existing_user_with_email or existing_user_with_username:
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with email or username already exists")
  
  new_user = User(email=body.email, username=body.username, password=body.password, role=body.role, location=body.location)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user


async def get_users(db:  Session = Depends(get_db)):
  return db.query(User).all()

async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
  user =  db.query(User).filter(User.id == user_id).first()
  if user is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  return user


async def update_user_by_id(user_id: int, body: UserDto, db: Session = Depends(get_db)):
  existing_user = db.query(User).filter(User.id == user_id).first()
  if existing_user is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
  
  # checking for user with the same email or username 
  existing_user_with_email = db.query(User).filter(User.email==body.email).first()
  existing_user_with_username = db.query(User).filter(User.username==body.username).first()
  if existing_user_with_email or existing_user_with_username:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with email or username already exists")
  
  existing_user.email = body.email
  existing_user.username = body.username
  db.commit()
  db.refresh(existing_user)
  return existing_user


async def delete_user_by_id(user_id: int,  db: Session = Depends(get_db)):
  existing_user = db.query(User).filter(User.id == user_id).first()
  if existing_user is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
  
  db.delete(existing_user)
  db.commit()
  return {"message": "User deleted"}


async def get_user_by_username_or_email(username_or_email: str, db: Session = Depends(get_db)):
  try:
    validate_email(username_or_email)
    query_filter = User.email
  except EmailNotValidError:
    query_filter = User.username
  user = db.query(User).filter(query_filter == username_or_email).first()
  return user


async def my_profile(token: str, db: Session = Depends(get_db)):
  decoded_token = await decode_access_token(token)
  user = db.query(User).filter(User.username == decoded_token['sub']).first()
  return user
