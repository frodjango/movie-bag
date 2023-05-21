from moviebag import create_app
import pytest



def test_hello(client):
    print("AKJDHFLKADHFLKJHDAFLKJADHFLKAJHSLKASDJH")
    response = client.get("/hello")
    assert response.data == b"<p>Hello, World!</p>"
