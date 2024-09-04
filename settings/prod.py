from .dev import *
URL_MAPS = {
    "0.0.0.0": [
        {"path": "/admin", "service": "172.17.0.1:8001"},
        {"path": "/static", "service": "172.17.0.1:8001"},
        {"path": "/api-admin", "service": "127.0.0.1:5000"},
        {"path": "", "service": "172.17.0.1:8000"},
    ],

}


PORT = 5000

RELOAD = False
WORKER = 1
