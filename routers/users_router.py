from fastapi import APIRouter,  Depends
from sqlalchemy.orm import Session
from dtos.user_dto import UserDto
from services import users_service
from database_config import get_db

router = APIRouter()


@router.post("/users")
async def create_user(body: UserDto, db: Session = Depends(get_db)):
  return await users_service.create_user(body, db)

@router.get("/users")
async def get_users(db: Session = Depends(get_db)):
  return await users_service.get_users(db)

@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
  return await users_service.get_user_by_id(user_id, db)

@router.patch("/users/{user_id}")
async def update_user_by_id(user_id: int, body: UserDto, db: Session = Depends(get_db)):
  return await users_service.update_user_by_id(user_id, body, db)