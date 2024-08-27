from utils.setting import UrlMaps


def find_service(maps: UrlMaps, path: str, domain: str):
    if (urls := maps.get(domain)) is not None:
        for url in urls:
            if path.startswith(url["path"]) and (
                len(path) == len(url["path"]) or path[len(url["path"])] == "/"
            ):
                return url["service"]
