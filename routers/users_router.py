from fastapi import APIRouter,  Depends
from sqlalchemy.orm import Session
from dtos.user_dto import UserDto
from services import users_service
from database_config import get_db
from api_responses.user_response import UserResponse
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login") # calling the bearer token

router = APIRouter()


@router.post("/users")
async def create_user(body: UserDto, db: Session = Depends(get_db)):
  return await users_service.create_user(body, db)

# applying the bearer token to the endpoint. the oauth2_scheme allows you to call the bearer token in the authorization header
##* note: dont put this endpoint after the endpoint with user_id path parameter
@router.get("/users/me", response_model=UserResponse)
async def my_profile(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  return await users_service.my_profile(token, db)

@router.get("/users", response_model=list[UserResponse])
async def get_users(db: Session = Depends(get_db)):
  return await users_service.get_users(db)

@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
  return await users_service.get_user_by_id(user_id, db)

@router.patch("/users/{user_id}")
async def update_user_by_id(user_id: int, body: UserDto, db: Session = Depends(get_db)):
  return await users_service.update_user_by_id(user_id, body, db)

@router.delete("/users/{user_id}")
async def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
  return await users_service.delete_user_by_id(user_id, db)
