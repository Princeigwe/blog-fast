from routers import (
  blogs_router, 
  users_router, 
  file_upload_router,
  auth_router,
  admin_dashboaard_router,
  article_router
  )
from fastapi import FastAPI
from database_config import Base, engine, SessionLocal

app = FastAPI(
  title="BlogFast",
  description="A simple blog API with FastAPI",
  version="0.1"
)

Base.metadata.create_all(engine) # create the tables in the database

app.include_router(blogs_router.router)
app.include_router(users_router.router)
app.include_router(file_upload_router.router)
app.include_router(auth_router.router)
app.include_router(admin_dashboaard_router.router)
app.include_router(article_router.router)

@app.get("/")
async def read_root():
  return {"Hello": "World"}
