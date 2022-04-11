from http import HTTPStatus

from flask import Blueprint, jsonify, request

from backend import schemas
from backend.repos.route import RouteRepo

view = Blueprint('route', __name__)

repo = RouteRepo()


@view.get('/')
def get_all():
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

    entity = repo.add(
        new_route.name,
        new_route.city_id,
        new_route.image,
        new_route.description,
        new_route.duration,
    )

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


@view.get('/<route_id>/points/')
def get_points(route_id):
    entities = repo.get_points(route_id)
    points = [schemas.RoutePoint.from_orm(entity).dict() for entity in entities]
    return jsonify(points), HTTPStatus.OK


@view.post('/<route_id>/places/')
def add_point(route_id):
    payload = request.json
    payload['uid'] = -1
    new_routepoint = schemas.RoutePoint(**payload)

    entity = repo.add_point(
        route_id,
        new_routepoint.position,
        new_routepoint.place_id,
        new_routepoint.distance,
    )

    new_routepoint = schemas.RoutePoint.from_orm(entity)
    return new_routepoint.dict(), HTTPStatus.CREATED


@view.delete('/<route_id>/places/<place_id>')
def delete_point(route_id, place_id):
    repo.delete_point(route_id, place_id)
    return {}, HTTPStatus.NO_CONTENT
