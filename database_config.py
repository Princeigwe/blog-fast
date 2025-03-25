from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# this class maintains a collection of all the defined tables for sqlalchemy orm functionality
# it is a base class for all the tables that are defined in the database
Base = declarative_base()

POSTGRES_USER=os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD=os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB=os.environ.get("POSTGRES_DB")
POSTGRES_HOST=os.environ.get("POSTGRES_HOST")
POSTGRES_PORT=os.environ.get("POSTGRES_PORT")

# DATABASE_URL = "sqlite:///./test.db" # test.db is the name of the database file
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL) # create a database engine

# variable responsible creating connection to the database engine, and  executing queries and retrieving data with sessionmaker.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# initializing database connection
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()