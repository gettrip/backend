import logging
import werkzeug.exceptions
import sqlalchemy.exc
from http import HTTPStatus
from http.client import BAD_REQUEST
from flask import jsonify, request, Blueprint
from backend.db import db_session
from uuid import uuid4
from backend.models import User
from backend.errors import Conflict

user = Blueprint('user', __name__)

logger = logging.getLogger(__name__)

""" create user """
@user.post('/')
def add_user():
    try:
        user_data = request.json
        uid = uuid4().hex
        new_user = User(uid = uid, name = user_data['name'])
        db_session.add(new_user)
        db_session.commit()
    except KeyError:
        return {"message": "user's data is incorrect"},  HTTPStatus.BAD_REQUEST
    except sqlalchemy.exc.IntegrityError:
        raise Conflict('user')
    return f'{new_user} successfully added', HTTPStatus.CREATED

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
        return {'message': 'user not found'}, HTTPStatus.NOT_FOUND
    return jsonify([{'name': user.name, 'uid': user.uid}]), HTTPStatus.OK

""" delete user """
@user.delete('/<uid>')
def delete_user(uid):
    user = User.query.filter(User.uid == uid).first()
    if not user:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND
    db_session.delete(user)
    db_session.commit()
    return {"message": "user was successfully deleted"}, HTTPStatus.OK

""" update user """
@user.put('/<uid>')
def update_user(uid):
    user = User.query.filter(User.uid == uid).first()
    if not user:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND
    try:
        new_data = request.json
        user.name = new_data['name']
        db_session.commit()
    except werkzeug.exceptions.BadRequest:
        return {"message": "user's data is incorrect"},  HTTPStatus.BAD_REQUEST
    except KeyError:
        return {"message": "user's data is incorrect"},  HTTPStatus.BAD_REQUEST
    except sqlalchemy.exc.IntegrityError:
        return {"message": "user already exist"}, HTTPStatus.UNPROCESSABLE_ENTITY
    except:
        logger.exception("message")
        return
    return f'{user} successfully updated', HTTPStatus.OK

