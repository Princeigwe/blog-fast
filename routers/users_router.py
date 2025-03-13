from fastapi import APIRouter,  Depends
from sqlalchemy.orm import Session
from dtos.user_dto import UserDto
from services import users_service
from database_config import get_db

router = APIRouter()

@router.post("/users")
async def create_user(user: UserDto, db: Session = Depends(get_db)):
  return await users_service.create_user(user, db)