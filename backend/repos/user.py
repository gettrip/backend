from backend.models import User
from backend.errors import Conflict, NotFound
from backend.db import db_session
from sqlalchemy.exc import IntegrityError
from typing import Optional


class UserRepo:

    def add(self, username: str) -> User:
        try:
            new_user = User(username=username)
            db_session.add(new_user)
            db_session.commit()
        except IntegrityError:
            raise Conflict('user')
        return new_user


    def get_all(self) -> list[User]:
        return User.query.all()

    def get_by_uid(self, uid: int) -> Optional[User]:
        user = User.query.filter(User.uid == uid).first()
        if not user:
            raise NotFound('user')
        return user

    def delete(self, uid: int) -> None:
        user = User.query.filter(User.uid == uid).first()
        if not user:
            raise NotFound('user')
        db_session.delete(user)
        db_session.commit()
        return None

    def update(self, uid: int, new_name: str) -> User:
        user = User.query.filter(User.uid == uid).first()
        if not user:
            raise NotFound('user')

        try: 
            user.username = new_name
            db_session.commit()    
        except IntegrityError:
            raise Conflict('user')
            
        return user