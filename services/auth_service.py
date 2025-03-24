from . import users_service
from database_config import get_db
from dtos.user_dto import UserDto
from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from services import users_service
from utils import jwt_encode_decode


async def register_user(body: UserDto, db: Session = Depends(get_db)):
  cipher = CryptContext(schemes="sha256_crypt")
  hashed_password = cipher.hash(body.password)

  print("plain  password", body.password)
  print("hashed password", hashed_password)
  body.password = hashed_password
  return await users_service.create_user(body, db)


async def authenticate_user(username_or_email: str, password: str, db: Session):
  cipher = CryptContext(schemes="sha256_crypt")
  user = await users_service.get_user_by_username_or_email(username_or_email, db)

  # if user does not exist or password decryption is incorrect
  if not user or not cipher.verify(password, user.password):
    raise HTTPException(status_code=403, detail="Invalid credentials")
  payload = {
    "sub": user.username
  }
  access_token = await jwt_encode_decode.create_access_token(payload)
  token_type = "bearer"
  return{
    "access_token": access_token, 
    "token_type": token_type
  }
