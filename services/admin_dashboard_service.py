from sqlalchemy.orm import Session
from utils.jwt_encode_decode import decode_access_token
from database_config import get_db
from fastapi import Depends, HTTPException, status
from services import users_service
from enums.roles_enums import Role


async def admin_dashboard(token: str, db: Session = Depends(get_db)):
  decoded_token = await decode_access_token(token)
  user = await users_service.get_user_by_username_or_email(decoded_token["sub"], db)
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  if user.role != Role.admin:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized access")
  return {
    "message": "Welcome to the admin dashboard"
  }