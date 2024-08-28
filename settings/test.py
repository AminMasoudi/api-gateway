
URL_MAPS = {
    "testserver": [
        {"path": "/admin", "service": "localhost:8081"},
        {"path": "", "service": "localhost:8080"},
        ],
}

DATABASE = {
    "drivername": "sqlite",
    "database": "test.sqlite3",
}

