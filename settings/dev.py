ROUTING_HOSTS = {

    "127.0.0.1" : [
        {"path": "/admin", "service": "127.0.0.1:8001"},
        {"path": "/static", "service": "127.0.0.1:8001"},
        {"path": "", "service":"127.0.0.1:5000"}
    ],
    "localhost":[
        {"path": "", "service": "localhost:8080"}
    ]
}
LOGGING = {
    
}

PORT = 8000