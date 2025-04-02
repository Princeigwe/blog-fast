from pydantic import BaseModel, Field

class ArticleDto(BaseModel):
  title: str | None = Field(max_length=300)
  content: str | None = Field(max_length=10000)