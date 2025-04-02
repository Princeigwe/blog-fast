from fastapi import Depends, HTTPException, status
from database_config import get_db
from sqlalchemy.orm import Session
from models.article_model import Article
from .users_service import my_profile


async def create_article(token: str, title: str, content: str, db: Session = Depends(get_db)):
  current_user = await my_profile(token, db)
  existing_article = db.query(Article).filter(
    Article.title == title, 
    Article.author_id ==current_user.id
    ).first()
  
  if existing_article:
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This title is not available")
  
  article = Article(title=title, content=content, author_id=current_user.id)
  db.add(article)
  db.commit()
  db.refresh(article)
  return article


async def get_articles(db: Session = Depends(get_db)):
  articles = db.query(Article).all()
  return articles

async def get_my_articles(token: str, db: Session = Depends(get_db)):
  try:
    current_user = await my_profile(token, db)
    articles = db.query(Article).filter(Article.author_id == current_user.id).all()
    return articles
  except Exception:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error fetching articles")


async def edit_article(token: str, article_id: int, title: str=None, content: str=None, db: Session = Depends(get_db)):
  current_user = await my_profile(token, db)
  existing_article = db.query(Article).filter(Article.id == article_id).first()
  if not existing_article:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
  elif existing_article.author_id != current_user.id:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized to modify article")
  
  existing_article.title = title if title else existing_article.title
  existing_article.content = content if content else existing_article.content
    
  db.commit()
  db.refresh(existing_article)
  return existing_article
