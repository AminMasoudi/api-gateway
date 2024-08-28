import pytest
import sqlalchemy as sa
from starlette.testclient import TestClient
from server import app as orig_app, get_call_client
from utils.http_client import MockClient

import os

from model.models import Base


@pytest.fixture()
def mock_db():
    DB_conf = {
        "drivername": "sqlite",
        "database": "test.sqlite3",
    }
    engine = sa.create_engine(sa.URL.create(
        **DB_conf
    ))
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)
    os.remove("test.sqlite3")


@pytest.fixture(scope="session")
def mock_call_client():
    def wraper():
        return MockClient()
    yield wraper

@pytest.fixture()
def client(mock_call_client):
    orig_app.dependency[get_call_client] = mock_call_client
    with TestClient(orig_app) as client:
        yield client

