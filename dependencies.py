
from utils.http_client import HttpxClient
import sqlalchemy as sa
from sqlalchemy import URL
from functools import lru_cache
from model import Base
from utils import settings

@lru_cache
def get_db(debug=False):
    DB_conf = settings.db_conf
    engine = sa.create_engine(URL.create(
        **DB_conf
    ))

    Base.metadata.create_all(engine)
    return engine

 

@lru_cache
def get_call_client():
    return HttpxClient()

