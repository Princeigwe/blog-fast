from fastapi import APIRouter, HTTPException
from dtos.blog_dto import BlogDto
from api_responses.blog_response import BlogResponse


router = APIRouter()

@router.post("/blogs")
async def create_blog(blog: BlogDto): # blog is the instance of Blog acting as a request body and will be validated by Pydantic
  return{"blog": blog}


@router.get("/blogs/error")
async def read_blogs_error():
  raise HTTPException(status_code=404, detail="Resource not found")

@router.get("/blogs", response_model=list[BlogResponse])
async def read_blogs(year: int=None): 
  '''
    The API response here has been customized with "list[BlogResponse]" to return
    a list of blogs with the years excluded.

    The read_blogs function returns a list of articles. The
    function accepts an optional year parameter. If the year
    parameter is provided, the function returns a list of
    articles from that year. If the year parameter is not
    provided, the function returns a list of all articles.

    year is an optional query parameter 
  '''
  # raising an HTTPException with status code 404 and detail "Resource not found" if the year is greater than 2025
  if year and year > 2025:
    raise HTTPException(status_code=404, detail="Resource not found")
  
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
