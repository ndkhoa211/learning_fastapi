from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create a location of db on FastAPI app
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# database engine is used to open up a connection and is able to use database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={'check_same_thread': False} # to allow multiple threads to access the database
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()