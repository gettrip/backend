import logging

from http import HTTPStatus
from flask import jsonify, request, Blueprint
from backend import schemas
from backend.repos.user import UserRepo


logger = logging.getLogger(__name__)

user = Blueprint('user', __name__)

repo = UserRepo()

""" create user """
@user.post('/')
def add_user():

    user_data = request.json
    user_data = schemas.User(**user_data)

    entity = repo.add(user_data.username)
    added_user = schemas.User.from_orm(entity)

    return added_user.dict(), HTTPStatus.CREATED

""" get all users """
@user.get('/')
def get_users():
    entitys = repo.get_all()
    entitys_lst = [{'username': entity.username, 'uid': entity.uid} for entity in entitys]
    return jsonify(entitys_lst), HTTPStatus.OK

""" get user by uid """
@user.get('/<uid>')
def get_by_id(uid):
    entity = repo.get_by_uid(uid)
    founded_user = schemas.User.from_orm(entity)
    return founded_user.dict(), HTTPStatus.OK

""" delete user """
@user.delete('/<uid>')
def delete_user(uid):
    repo.delete(uid)    
    return {"message": "user was successfully deleted"}, HTTPStatus.NO_CONTENT

""" update user """
@user.put('/<uid>')
def update_user(uid):
    user_data = request.json
    user_data = schemas.User(**user_data)
    
    entity = repo.update(uid, user_data.username)
    updated_user = schemas.User.from_orm(entity)

    return updated_user.dict(), HTTPStatus.OK