from utils import settings
import pytest


def test_setting_url_maps_is_sorted():

    maps = settings.url_maps
    for host, paths in maps.items():
        for i in range(len(paths) - 1):
            assert paths[i]["path"] > paths[i+1]["path"]




class TestRouting:
    def test_find_service_by_path(self):
        ...    

    def test_find_service_by_host(self):
        ...
