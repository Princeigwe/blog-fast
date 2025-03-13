from pydantic  import BaseModel, Field

class BlogDto(BaseModel):
  title: str = Field(..., example="My first article", min_length=1, max_length=100)
  author: str = Field(..., example="Prince Igwe", min_length=1, max_length=100)
  year: int = Field(..., example=2022, gt=2022, lt=2026)