from http import HTTPStatus

from flask import Blueprint, jsonify, request

from backend import schemas
from backend.repos.place import PlaceRepo

view = Blueprint('place', __name__)

repo = PlaceRepo()


@view.get('/')
def get_all():
    entities = repo.get_all()
    places = [schemas.Place.from_orm(entity).dict() for entity in entities]
    return jsonify(places), HTTPStatus.OK


@view.get('/<uid>')
def get_by_id(uid):
    entity = repo.get_by_id(uid)
    place = schemas.Place.from_orm(entity)
    return place.dict(), HTTPStatus.OK


@view.post('/')
def add_place():
    payload = request.json
    payload['uid'] = -1
    new_place = schemas.Place(**payload)

    entity = repo.add(
        new_place.name,
        new_place.city_id,
        new_place.image,
        new_place.description,
        new_place.duration,
    )

    new_place = schemas.Place.from_orm(entity)
    return new_place.dict(), HTTPStatus.CREATED


@view.put('/<uid>')
def update_place(uid):
    payload = request.json
    payload['uid'] = uid
    new_place = schemas.Place(**payload)

    entity = repo.update(**new_place.dict())

    new_place = schemas.Place.from_orm(entity)
    return new_place.dict(), HTTPStatus.OK


@view.delete('/<uid>')
def delete_place(uid):
    repo.delete(uid)
    return {}, HTTPStatus.NO_CONTENT
