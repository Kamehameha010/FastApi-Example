from fastapi import APIRouter, Depends, Response

from schemes.user import User, UserCreate, UserUpdate
from starlette.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
)
from db.query import DbUserContext


user_router = APIRouter()


@user_router.get("/users", response_model=list[User])
def get_all(skip: int = 0, limit: int = 10, db: DbUserContext = Depends(DbUserContext)):
    return db.get_users(skip, limit)


@user_router.post("/users", status_code=HTTP_204_NO_CONTENT | HTTP_400_BAD_REQUEST)
def create_user(user: UserCreate, db: DbUserContext = Depends(DbUserContext)):
    db.create_user(user)
    return HTTP_204_NO_CONTENT


@user_router.get("/users/{id}", response_model=User | None)
def get_user_by_id(id: int, db: DbUserContext = Depends(DbUserContext)):
    return db.get_user_by_id(id)


@user_router.put("/users/{id}", status_code=HTTP_204_NO_CONTENT)
def update_user(
    userid: int, user: UserUpdate, db: DbUserContext = Depends(DbUserContext)
):
    db.update_user(userid, user)
    return HTTP_204_NO_CONTENT


@user_router.delete("/users/{id}")
def delete_user(userid: int, db: DbUserContext = Depends(DbUserContext)):
    db.delete_user(userid)
    return HTTP_204_NO_CONTENT
