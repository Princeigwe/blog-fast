from fastapi import APIRouter
from models.blog_model import Blog


router = APIRouter()

@router.post("/blogs")
async def create_blog(blog: Blog): # blog is the instance of Blog acting as a request body and will be validated by Pydantic
  return{"blog": blog}

@router.get("/blogs")
async def read_blogs(year: int=None): # year is an optional query parameter 
  if year: # if year is provided, return a list of articles from that year
    return [
      {
        "year": year,
        "title": "My first article",
        "author": "Prince Igwe"
      }
    ]
  else:
    return [
      {
        "year": 2021,
        "title": "My first article",
        "author": "Prince Igwe"
      },
      {
        "year": 2021,
        "title": "My second article",
        "author": "Prince Igwe"
      },
      {
        "year": 2023,
        "title": "My third article",
        "author": "Prince Igwe"
      }
    ]

@router.get("/blogs/{blog_id}")
async def read_blog(blog_id: int):
  return {"blog_id": blog_id}
