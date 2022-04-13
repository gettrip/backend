import logging
from http import HTTPStatus

from flask import Blueprint, jsonify, request

from backend import schemas
from backend.auth import auth
from backend.repos.user import UserRepo

logger = logging.getLogger(__name__)

user = Blueprint('user', __name__)

repo = UserRepo()


@user.post('/')
def add_user():

    user_data = request.json
    user_data = schemas.User(**user_data)

    entity = repo.add(user_data.username)
    added_user = schemas.User.from_orm(entity)

    return added_user.dict(), HTTPStatus.CREATED


@user.get('/')
def get_users():
    entities = repo.get_all()
    users = [schemas.User.from_orm(entity).dict() for entity in entities]
    return jsonify(users), HTTPStatus.OK


@user.get('/<uid>')
def get_by_id(uid):
    entity = repo.get_by_uid(uid)
    founded_user = schemas.User.from_orm(entity)
    return founded_user.dict(), HTTPStatus.OK


@user.delete('/<uid>')
@auth.login_required
def delete_user(uid):
    repo.delete(uid)
    return {}, HTTPStatus.NO_CONTENT


@user.put('/<uid>')
def update_user(uid):
    user_data = request.json
    user_data = schemas.User(**user_data)

    entity = repo.update(uid, user_data.username)
    updated_user = schemas.User.from_orm(entity)

    return updated_user.dict(), HTTPStatus.OK
