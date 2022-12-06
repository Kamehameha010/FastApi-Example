from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLARCHEMY_DATABASE_URL = os.getenv("SQLARCHEMY_DATABASE_URL")

engine = create_engine(SQLARCHEMY_DATABASE_URL)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
