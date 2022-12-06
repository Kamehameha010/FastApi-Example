from typing import Generator, List
from sqlalchemy.orm import Session
import schemes
import models
from .base import Base, engine, session_local


class DbUserContext:
    _db: Session

    def __init__(self) -> None:
        self.__initialize_db()
        self._db = self._get_db()

    def __initialize_db(self):
        Base.metadata.create_all(engine)

    def _get_db(self) -> Generator[Session, None, None]:
        db = session_local()
        try:
            yield db
        finally:
            db.close()

    def create_user(self, user: schemes.UserCreate) -> None:
        with session_local() as db:
            db_user = models.User(**user.dict())
            db.add(db_user)
            db.commit()

    def get_users(self, skip: int = 0, limit: int = 10) -> List[models.User]:
        with session_local() as db:
            return db.query(models.User).offset(skip).limit(limit).all()

    def get_user_by_id(self, userid: int) -> models.User | None:
        with session_local() as db:
            return db.query(models.User).get(userid)

    def delete_user(self, userid: int) -> None:
        with session_local() as db:
            user = db.query(models.User).get(userid)
            db.delete(user)
            db.commit()

    def update_user(self, userid: int, user: schemes.UserUpdate) -> None:
        with session_local() as db:
            db.query(models.User).filter_by(id=userid).update(
                {
                    models.User.is_active: user.is_active,
                    models.User.name: user.name,
                    models.User.lastname: user.lastname,
                    models.User.username: user.username,
                    models.User.password: user.password,
                }
            )
            db.commit()
