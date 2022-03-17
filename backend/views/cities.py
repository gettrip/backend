import logging
from http import HTTPStatus

from flask import Blueprint, jsonify, request

from backend import schemas
from backend.repos.cities import CityRepo

logger = logging.getLogger(__name__)

view = Blueprint('cities', __name__)

repo = CityRepo()


@view.get('/')
def get_cities():
    entities = repo.get_all()
    cities = [schemas.City.from_orm(entity).dict() for entity in entities]
    return jsonify(cities), HTTPStatus.OK


@view.get('/<uid>')
def get_by_id(uid):
    entity = repo.get_by_id(uid)
    city = schemas.City.from_orm(entity)
    return city.dict(), HTTPStatus.OK


@view.post('/')
def add_city():
    payload = request.json
    payload['uid'] = -1
    new_city = schemas.City(**payload)

    entity = repo.add(new_city.name)

    new_city = schemas.City.from_orm(entity)
    return new_city.dict(), HTTPStatus.CREATED


@view.put('/<uid>')
def update_city(uid):
    payload = request.json
    payload['uid'] = uid
    new_city = schemas.City(**payload)

    entity = repo.update(**new_city.dict())

    new_city = schemas.City.from_orm(entity)
    return new_city.dict(), HTTPStatus.OK


@view.delete('/<uid>')
def delete_city(uid):
    repo.delete(uid)
    return {}, HTTPStatus.NO_CONTENT
