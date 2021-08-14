from werkzeug.wrappers import response
from covidanalyser import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hellp(client):
    response = client.get('/hello')
    assert response.data == b'Hellp, World!'