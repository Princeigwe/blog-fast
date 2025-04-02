from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services import article_service
from fastapi.security import OAuth2PasswordBearer
from dtos.article_dto import ArticleDto
from database_config import get_db
from services.users_service import my_profile
from enums.roles_enums import Role 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


router = APIRouter()


@router.post("/articles")
async def create_article(body: ArticleDto, token: str= Depends(oauth2_scheme), db: Session = Depends(get_db)):
  return await article_service.create_article(token, body.title, body.content, db)


@router.get("/articles")
async def get_articles(token: str= Depends(oauth2_scheme), db: Session = Depends(get_db)):
  current_user = await my_profile(token, db)
  if current_user.role != Role.admin:
    print("Normal user")
    return await article_service.get_my_articles(token, db)
  else:
    print("Admin user")
    return await article_service.get_articles(db)

@router.patch("/articles/{article_id}")
async def edit_article(article_id: int, body: ArticleDto, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  return await article_service.edit_article(token, article_id, body.title, body.content, db)