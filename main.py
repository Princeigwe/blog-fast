from routers import blogs_router, users_router, file_upload_router
from fastapi import FastAPI
from database_config import Base, engine, SessionLocal

app = FastAPI()

Base.metadata.create_all(engine) # create the tables in the database

app.include_router(blogs_router.router)
app.include_router(users_router.router)
app.include_router(file_upload_router.router)

@app.get("/")
async def read_root():
  return {"Hello": "World"}
