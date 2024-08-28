from utils import settings
import pytest
from starlette.testclient import TestClient
from server import app as orig_app
from utils.http_client import MockClient


@pytest.fixture
def client():
    orig_app.dependency.call_client = MockClient()
    with TestClient(orig_app) as client:
        yield client




class TestRouting:
    def test_find_service_by_path(self):
        ...    

    def test_find_service_by_host(self):
        ...



def test_foo(client):
    response  = client.get("/foo")
    assert response.content == b"mock"