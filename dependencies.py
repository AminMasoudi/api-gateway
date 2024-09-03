from functools import lru_cache


# from models import Base
from utils import settings
from utils.http_client import HttpxClient

 

@lru_cache
def get_call_client():
    return HttpxClient()

