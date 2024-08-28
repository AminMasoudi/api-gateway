import os
import importlib
from functools import lru_cache
from typing import NewType


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

        self.preprocessing()

    def preprocessing(self):
        # preprocessing on URL_MAPS
        url_maps: UrlMaps = getattr(self, "URL_MAPS")
        for k, v in url_maps.items():
            url_maps[k].sort(key=lambda x: x["path"], reverse=True)
        self.__url_maps = url_maps

    @lru_cache
    def get_url_maps(self) -> UrlMaps:
        return self.__url_maps

    @property
    def db(self):
        return self.__db


settings = Settings()
