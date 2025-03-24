from . import users_service
from database_config import get_db
from dtos.user_dto import UserDto
from fastapi import Depends
from passlib.context import CryptContext
from sqlalchemy.orm import Session

async def register_user(body: UserDto, db: Session = Depends(get_db)):
  cipher = CryptContext(schemes="sha256_crypt")
  hashed_password = cipher.hash(body.password)
  print("plain  passwoord", body.password)
  print("hashed password", hashed_password)
  body.password = hashed_password
  return await users_service.create_user(body, db)