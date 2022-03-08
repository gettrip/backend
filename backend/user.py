import logging
import sqlalchemy.exc

from http import HTTPStatus
from flask import jsonify, request, Blueprint
from backend.db import db_session
from uuid import uuid4
from backend.models import User
from backend.errors import Conflict, NotFound, NotValid
from backend import schemas
from pydantic import ValidationError

user = Blueprint('user', __name__)

logger = logging.getLogger(__name__)


""" create user """
@user.post('/')
def add_user():

    user_data = request.json

    try:
        user_data = schemas.User(**user_data)
    except ValidationError:
        raise NotValid('user')

    try:
        uid = uuid4().hex
        new_user = User(name=user_data.name, uid=uid)
        db_session.add(new_user)
        db_session.commit()
    except sqlalchemy.exc.IntegrityError:
        raise Conflict('user')

    added_user = schemas.User.from_orm(new_user)

    return added_user.dict(), HTTPStatus.CREATED

""" get all users """
@user.get('/')
def get_users():
    all_users = User.query.all()
    all_users_lst = [{'name': user.name, 'uid': user.uid} for user in all_users ]
    return jsonify(all_users_lst), HTTPStatus.OK

""" get user by uid """
@user.get('/<uid>')
def get_by_id(uid):
    user = User.query.filter(User.uid == uid).first()
    if not user:
        raise NotFound('user')

    founded_user = schemas.User.from_orm(user)

    return founded_user.dict(), HTTPStatus.OK

""" delete user """
@user.delete('/<uid>')
def delete_user(uid):
    user = User.query.filter(User.uid == uid).first()
    if not user:
        return {}, HTTPStatus.NO_CONTENT
    db_session.delete(user)
    db_session.commit()
    return {"message": "user was successfully deleted"}, HTTPStatus.OK

""" update user """
@user.put('/<uid>')
def update_user(uid):
    user = User.query.filter(User.uid == uid).first()

    if not user:
        raise NotFound('user')

    user_data = request.json
    
    try:
        user_data = schemas.User(**user_data)
    except ValidationError:
        raise NotValid('user')


    try: 
        user.name = user_data.name
        db_session.commit()    
    except sqlalchemy.exc.IntegrityError:
        raise Conflict('user')

    updated_user = schemas.User.from_orm(user)

    return updated_user.dict(), HTTPStatus.OK

