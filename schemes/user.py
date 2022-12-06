from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    lastname: str
    username: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: str
    is_active: bool


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
