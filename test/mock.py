import os

import pytest
# import sqlalchemy as sa
from starlette.testclient import TestClient

from server import app as orig_app, get_call_client
from utils.http_client import MockClient
# from models import Base



@pytest.fixture()
def mock_call_client():
    def wraper():
        return MockClient()

    yield wraper


@pytest.fixture()
def client(mock_call_client):
    orig_app.dependency[get_call_client] = mock_call_client
    with TestClient(orig_app) as client:
        setattr(client, "call_client", mock_call_client())
        yield client
