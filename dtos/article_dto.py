from pydantic import BaseModel, Field

class ArticleDto(BaseModel):
  title: str = Field(max_length=300)
  content: str = Field(max_length=10000)