from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# this class maintains a collection of all the defined tables for sqlalchemy orm functionality
# it is a base class for all the tables that are defined in the database
Base = declarative_base()


DATABASE_URL = "sqlite:///./test.db" # test.db is the name of the database file

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