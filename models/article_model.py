from database_config  import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Article(Base):
  __tablename__ = 'article'
  id: Mapped[int] = mapped_column(primary_key=True, index=True)
  title: Mapped[str] = mapped_column(String(300))
  content: Mapped[str]= mapped_column(String(10000))
  is_published: Mapped[bool] = mapped_column(default=False)
  created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
  published_at :Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

  author_id: Mapped[int] = mapped_column(ForeignKey("user.id")) # user foreign key
