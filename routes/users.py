from fastapi import APIRouter

from models.user import User

user_router = APIRouter()


@user_router.get("/users", response_model=list[User])
def get_all(skip: int = 0, limit:int = 10 ):
    return ""


@user_router.get("/users/{id}", response_model=list[User])
def get_user_by_id(id: str):
    return ""
