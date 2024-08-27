import os
import importlib
from functools import lru_cache
from typing import NewType

from utils.http_client import AbstractClient, HttpxClient
from model.database import get_db

UrlMaps = NewType("UrlMaps", dict[str, list[dict[str, str]]])
class Settings:
    def __init__(self) -> None:
        settings_module = os.environ.get("SETTINGS")
        mod = importlib.import_module(settings_module)
        assert "URL_MAPS" in dir(mod)
        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)
                setattr(self, setting, setting_value)

        self.__call_client = HttpxClient()
        self.__db = get_db(debug=True)
        self.preprocessing()

    def preprocessing(self):
        # preprocessing on URL_MAPS
        url_maps:UrlMaps = getattr(self, "URL_MAPS")
        for k, v in url_maps.items():
            url_maps[k].sort(key=lambda x: x["path"], reverse=True)
        self.__url_maps = url_maps

    @property
    @lru_cache
    def url_maps(self) -> UrlMaps:
        return self.__url_maps

    @property
    def call_client(self) -> AbstractClient:
        return self.__call_client
    
    @call_client.setter
    def set_call_client(self, Client:AbstractClient):
        assert isinstance(Client, AbstractClient)
        self.__call_client = Client

    @property
    def db(self):
        return self.__db
    
    
settings = Settings()
