from tests.factories import CityFactory, RouteFactory
import random
from backend.config import config

def test_add_city_successed(client, session):
    city_data = {'name': 'test_city', 'image': 'test_url'}
    response = client.post('/api/v1/cities/', json=city_data)
    assert response.status_code == 201


def test_add_city_failed_notvalid(client, session):
    city_data = {'cityname': 'test_city', 'image': 'test_url'}
    response = client.post('/api/v1/cities/', json=city_data)
    assert response.status_code == 400


def test_get_city_by_uid_successed(client, session):
    cities = []
    for _ in range(10):
        city = CityFactory.create()
        cities.append(city)
    city_id = int(cities[random.randint(0,9)].uid)

    response = client.get(f'/api/v1/cities/{city_id}')
    assert response.status_code == 200

    recieved_city = response.json
    assert recieved_city['uid'] == city_id


def test_get_city_by_uid_failed_notfound(client, session):
    cities = []
    for _ in range(10):
        city = CityFactory.create()
        cities.append(city)
    city_id = int(cities[-1].uid) + 1

    response = client.get(f'/api/v1/cities/{city_id}')
    assert response.status_code == 404


def test_get_all_cities_successed(client, session):
    numb = 10
    cities = []
    for _ in range(numb):
        new_city = CityFactory.create()
        cities.append(new_city)

    response = client.get('/api/v1/cities/')
    assert response.status_code == 200

    recieved_cities = response.json
    assert len(recieved_cities) == numb

    for i in range(numb):
        assert cities[i].name == recieved_cities[i]['name']


def test_update_city_successed(client, session):
    city = CityFactory.create()
    city_data = {'name': 'test_city', 'image': 'test_url'}

    response = client.put(f'/api/v1/cities/{city.uid}', json=city_data)
    assert response.status_code == 200

    assert city.name == 'test_city'


def test_update_city_failed_notvalid(client, session):
    city = CityFactory.create()
    city_data = {'cityname': 'test_city', 'image': 'test_url'}

    response = client.put(f'/api/v1/cities/{city.uid}', json=city_data)
    assert response.status_code == 400


def test_get_routes_successed(client, session):
    city1 = CityFactory.create()
    city2 = CityFactory.create()
    n_routes = [5, 7]
    cities = [city1, city2]

    for i in range(2):

        routes = []
        for _ in range(n_routes[i]):
            route = RouteFactory.create()
            route.city_id = cities[i].uid
            routes.append(route)

        response = client.get(f'/api/v1/cities/{cities[i].uid}/routes/')
        assert response.status_code == 200

        recieved_routes = response.json
        assert len(recieved_routes) == n_routes[i]

        for j in range(n_routes[i]):
            assert recieved_routes[j]['name'] == routes[j].name


def test_delete_city_successed(client, session):
    numb = 10
    cities = []
    for _ in range(numb):
        new_city = CityFactory.create()
        cities.append(new_city)

    headers = {"Authorization": f"Bearer {config.server.token}"}
    response = client.delete(f'/api/v1/cities/{cities[0].uid}', headers=headers)
    assert response.status_code == 204

    response = client.get('/api/v1/cities/')
    assert response.status_code == 200

    recieved_cities = response.json
    assert len(recieved_cities) == numb - 1


def test_delete_city_failed_unauthorized_wrong_token(client, session):
    city = CityFactory.create()
    headers = {
        "Authorization": f"Bearer abcd"
    }
    response = client.delete(f'/api/v1/cities/{city.uid}', headers=headers)
    assert response.status_code == 401


def test_delete_city_failed_unauthorized_without_token(client, session):
    city = CityFactory.create()
    response = client.delete(f'/api/v1/cities/{city.uid}')
    assert response.status_code == 401



