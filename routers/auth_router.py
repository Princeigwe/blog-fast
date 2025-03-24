from dtos.user_dto import UserDto
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services import auth_service
from database_config import get_db

router = APIRouter()


@router.post("/auth/register")
async def register_user(body: UserDto, db: Session = Depends(get_db)):
  return await auth_service.register_user(body, db)