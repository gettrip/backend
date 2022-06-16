import flask
from sqlalchemy.exc import IntegrityError

from backend.db import get_db
from backend.errors import ConflictError, NotFoundError
from backend.models import User


class UserRepo:
    name = 'user'

    def add(self, username: str) -> User:
        try:
            new_user = User(username=username)
            db_session = get_db(flask.current_app.config['db']['url'])
            db_session.add(new_user)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)
        return new_user

    def get_all(self) -> list[User]:
        return User.query.all()

    def get_by_uid(self, uid: int) -> User:
        user = User.query.filter(User.uid == uid).first()
        if not user:
            raise NotFoundError(self.name)
        return user

    def delete(self, uid: int) -> None:
        user = User.query.filter(User.uid == uid).first()
        if not user:
            raise NotFoundError(self.name)
        db_session = get_db(flask.current_app.config['db']['url'])
        db_session.delete(user)
        db_session.commit()

    def update(self, uid: int, new_name: str) -> User:
        user = User.query.filter(User.uid == uid).first()
        if not user:
            raise NotFoundError(self.name)

        try:
            user.username = new_name
            db_session = get_db(flask.current_app.config['db']['url'])
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return user
