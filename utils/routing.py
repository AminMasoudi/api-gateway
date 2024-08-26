from utils.setting import settings

def router(path:str, domain:str):
    maps = settings.url_maps
    return find_service(maps, path, domain)


def find_service(maps: dict[str, list[dict[str, str]]], path: str, domain: str):
    if (urls := maps.get(domain)) is not None:
        for url in urls:
            if path.startswith(url["path"]):
                return url["service"]
