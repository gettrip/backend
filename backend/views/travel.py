from http import HTTPStatus

from flask import Blueprint, jsonify, request

from backend import schemas
from backend.repos.travel import TravelRepo

view = Blueprint('travel', __name__)

repo = TravelRepo()


@view.get('/')
def get_all():
    entities = repo.get_all()
    travels = [schemas.Travel.from_orm(entity).dict() for entity in entities]
    return jsonify(travels), HTTPStatus.OK


@view.get('/<uid>')
def get_by_id(uid):
    entity = repo.get_by_id(uid)
    travel = schemas.Travel.from_orm(entity)
    return travel.dict(), HTTPStatus.OK


@view.post('/')
def add_travel():
    payload = request.json
    payload['uid'] = -1
    new_travel = schemas.Travel(**payload)

    entity = repo.add(
        new_travel.name,
        new_travel.city_id,
        new_travel.user_id,
    )

    new_travel = schemas.Travel.from_orm(entity)
    return new_travel.dict(), HTTPStatus.CREATED


@view.put('/<uid>')
def update_travel(uid):
    payload = request.json
    payload['uid'] = uid
    new_travel = schemas.Travel(**payload)

    entity = repo.update(**new_travel.dict())

    new_travel = schemas.Travel.from_orm(entity)
    return new_travel.dict(), HTTPStatus.OK


@view.delete('/<uid>')
def delete_travel(uid):
    repo.delete(uid)
    return {}, HTTPStatus.NO_CONTENT
