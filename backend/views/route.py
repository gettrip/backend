import logging
from http import HTTPStatus
from random import randint

from flask import Blueprint, jsonify, request

from backend import schemas
from backend.repos.route import RouteRepo

logger = logging.getLogger(__name__)

view = Blueprint('route', __name__)

repo = RouteRepo()


@view.get('/')
def get_route():
    entities = repo.get_all()
    routes = [schemas.Route.from_orm(entity).dict() for entity in entities]
    return jsonify(routes), HTTPStatus.OK


@view.get('/<uid>')
def get_by_id(uid):
    entity = repo.get_by_id(uid)
    route = schemas.Route.from_orm(entity)
    return route.dict(), HTTPStatus.OK


@view.post('/')
def add_route():
    payload = request.json
    payload['uid'] = -1
    new_route = schemas.Route(**payload)

    entity = repo.add(new_route.name, new_route.city_id)

    new_route = schemas.Route.from_orm(entity)
    return new_route.dict(), HTTPStatus.CREATED


@view.put('/<uid>')
def update_route(uid):
    payload = request.json
    payload['uid'] = uid
    new_route = schemas.Route(**payload)

    entity = repo.update(**new_route.dict())

    new_route = schemas.Route.from_orm(entity)
    return new_route.dict(), HTTPStatus.OK


@view.delete('/<uid>')
def delete_route(uid):
    repo.delete(uid)
    return {}, HTTPStatus.NO_CONTENT


@view.get('/1/places/')
def get_routeplaces():
    entities = repo.get_all_routplaces()
    routeplaces = [schemas.RoutePlace.from_orm(entity).dict() for entity in entities]
    return jsonify(routeplaces), HTTPStatus.OK


@view.post('/1/places/')
def add_routeplace():
    payload = request.json
    payload['uid'] = -1
    payload['distance'] = randint(100, 1000)
    new_routeplace = schemas.RoutePlace(**payload)

    entity = repo.add_routeplace(
        new_routeplace.route_id,
        new_routeplace.position,
        new_routeplace.place_id,
        new_routeplace.distance,
    )

    new_routeplace = schemas.RoutePlace.from_orm(entity)
    return new_routeplace.dict(), HTTPStatus.CREATED


@view.delete('/1/places/')
def delete_routeplace():
    payload = request.json
    logger.info(payload)
    repo.delete_routeplace(**payload)
    return {}, HTTPStatus.NO_CONTENT
