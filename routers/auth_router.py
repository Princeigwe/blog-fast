from dtos.user_dto import UserDto
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services import auth_service
from database_config import get_db
from api_responses.token_response import TokenResponse
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/auth/register")
async def register_user(body: UserDto, db: Session = Depends(get_db)):
  return await auth_service.register_user(body, db)


@router.post("/auth/login", response_model=TokenResponse)
async def login_user( form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)  ):
  return await auth_service.authenticate_user(form_data.username, form_data.password, db)