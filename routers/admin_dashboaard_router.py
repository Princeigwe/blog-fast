from fastapi import APIRouter
from services import admin_dashboard_service
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from sqlalchemy.orm import Session
from database_config import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
router = APIRouter()

@router.get("/admin-dashboard")
async def admin_dashboard(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  return await admin_dashboard_service.admin_dashboard(token, db)