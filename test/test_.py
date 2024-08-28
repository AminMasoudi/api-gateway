from .mock import mock_call_client, client, get_call_client


def test_(client):
    response  = client.get("/foo")
    assert response.content == b"mock"