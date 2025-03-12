from pydantic import BaseModel

class BlogResponse(BaseModel):
  title: str
  author: str