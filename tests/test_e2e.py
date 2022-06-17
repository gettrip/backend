from tests.factories import CityFactory


def test_get_all_cities_returned(client, session):
    city = CityFactory.create()

    response = client.get('/api/v1/cities/')
    assert response.status_code == 200

    cities = response.json
    assert len(cities) == 1
    assert cities[0]['name'] == city.name


def test_get_all_cities_returned2(client, session):
    city = CityFactory.create()

    response = client.get('/api/v1/cities/')
    assert response.status_code == 200

    cities = response.json
    assert len(cities) == 1
    assert cities[0]['name'] == city.name
