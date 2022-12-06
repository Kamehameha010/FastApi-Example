from sqlalchemy import Boolean, Column, Integer, String
from db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    lastname = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
