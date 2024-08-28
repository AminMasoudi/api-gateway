from functools import lru_cache

import sqlalchemy as sa

from models import Base
from utils import settings
from utils.http_client import HttpxClient

@lru_cache
def get_db():
    DB_conf = settings.db_conf
    engine = sa.create_engine(sa.URL.create(
        **DB_conf
    ))

    Base.metadata.create_all(engine)
    return engine

 

@lru_cache
def get_call_client():
    return HttpxClient()

