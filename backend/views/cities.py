from http import HTTPStatus

from flask import Blueprint, jsonify, request

from backend import schemas
from backend.auth import auth
from backend.repos.cities import CityRepo
from backend.repos.route import RouteRepo

view = Blueprint('cities', __name__)

city_repo = CityRepo()
route_repo = RouteRepo()


@view.get('/')
def get_all():
    entities = city_repo.get_all()
    cities = [schemas.City.from_orm(entity).dict() for entity in entities]
    return jsonify(cities), HTTPStatus.OK


@view.get('/<uid>')
def get_by_id(uid):
    entity = city_repo.get_by_id(uid)
    city = schemas.City.from_orm(entity)
    return city.dict(), HTTPStatus.OK


@view.get('/<uid>/routes/')
def get_routes(uid):
    entities = route_repo.get_by_city(uid)
    routes = [schemas.Route.from_orm(entity).dict() for entity in entities]
    return jsonify(routes), HTTPStatus.OK


@view.post('/')
def add_city():
    payload = request.json
    payload['uid'] = -1
    new_city = schemas.City(**payload)

    entity = city_repo.add(new_city.name, new_city.image)

    new_city = schemas.City.from_orm(entity)
    return new_city.dict(), HTTPStatus.CREATED


@view.put('/<uid>')
def update_city(uid):
    payload = request.json
    payload['uid'] = uid
    new_city = schemas.City(**payload)

    entity = city_repo.update(**new_city.dict())

    new_city = schemas.City.from_orm(entity)
    return new_city.dict(), HTTPStatus.OK


@view.delete('/<uid>')
@auth.login_required
def delete_city(uid):
    city_repo.delete(uid)
    return {}, HTTPStatus.NO_CONTENT
