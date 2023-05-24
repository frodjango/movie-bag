# from moviebag import create_app
# import pytest



def test_hello(client):
    response = client.get("/hello")
    assert response.data == b"<p>Hello, World!</p>"

def test_index(client):
    response = client.get("/")
    assert response.data == b"<p>Salut Fro - index !</p>"
