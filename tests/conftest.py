import json

import pytest

from backend.app import create_app


@pytest.fixture
def app():
    test_app = create_app(testing=True)
    yield test_app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def clear_database(client):
    resp = client.get('/api/v1/cities/')
    all_cities = json.loads(resp.data.decode())
    for city in all_cities:
        city_uid = city['uid']
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype,
        }
        client.delete(f'/api/v1/cities/{city_uid}', data={}, headers=headers)


@pytest.fixture()
def fill_database(client):
    for city_number in range(1):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype,
        }
        citydata = {
            'name': f'city{city_number}',
            'image': 'abc',
        }
        # data=json.dumps(citydata)
        client.post('/api/v1/cities/', headers=headers, data=json.dumps(citydata))
