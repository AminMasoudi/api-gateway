import sqlalchemy as sa
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker
from functools import lru_cache
from .models import Base
import os


@lru_cache
def get_db(debug=False):

    if debug:
       DB = sa.create_engine("sqlite:///db.sqlite3")

    else:
        DB_conf = {
            "drivername":"mysql+pymysql",
            "database": os.environ.get("MYSQL_DB"),
            "host":os.environ.get("DB_URL", "mysql"),
            "password":os.environ.get("MYSQL_PASSWORD"),
            "port":int(os.environ.get("MYSQL_PORT", "3306")),
            "username":os.environ.get("MYSQL_USER"),
            }
        DB = db_connection(**DB_conf)

    Base.metadata.create_all(DB)
    Session = sessionmaker(DB)
    return Session

 
def db_connection(**kwargs):
    return sa.create_engine(URL.create(
        **kwargs
    ))