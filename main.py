from routers import blogs_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(blogs_router.router)

@app.get("/")
async def read_root():
  return {"Hello": "World"}
