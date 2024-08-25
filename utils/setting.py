import os
import importlib
from functools import lru_cache

class Settings:
    def __init__(self) -> None:
        settings_module = os.environ.get("SETTINGS")
        mod = importlib.import_module(settings_module)
        assert "ROUTING_HOSTS" in dir(mod)
        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)
                setattr(self, setting, setting_value)
        self.preprocessing()

    def preprocessing(self):
        # preprocessing on ROUTING_HOSTS
        routing_hosts = getattr(self, "ROUTING_HOSTS")
        for k, v in routing_hosts.items():
            routing_hosts[k].sort(key=lambda x: x["path"], reverse=True)
        self.__routing_hosts = routing_hosts

    @property
    @lru_cache
    def routing_hosts(self):
        return self.__routing_hosts


settings = Settings()
