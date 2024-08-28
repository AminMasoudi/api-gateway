URL_MAPS = {
    "127.0.0.1": [
        {"path": "/admin", "service": "127.0.0.1:8001"},
        {"path": "/static", "service": "127.0.0.1:8001"},
        {"path": "/api-admin", "service": "127.0.0.1:5000"},
        {"path": "", "service": "127.0.0.1:5000"},
    ],
    "testserver": [{"path": "", "service": "localhost:8080"}],
}
LOGGING = {}

PORT = 8000

ADMIN = True
ADMIN_PORT = 5000