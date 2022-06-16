import json


def test_get_all_cities(fill_database, clear_database, client):
    clear_database
    fill_database
    resp = client.get('/api/v1/cities/')
    data = json.loads(resp.data.decode())
    assert data == ['1']
