from fastapi import APIRouter
router = APIRouter()

@router.get("/authors")
async def get_authors():
  return [
    {"id": 1, "name": "Mark Twain"},
    {"id": 2, "name": "Jane Austen"},
    {"id": 3, "name": "Charles Dickens"}
  ]

@router.get("/authors/{author_id}")
async def get_author(author_id: int):
  return {"author_id": author_id} 