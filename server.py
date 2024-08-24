from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route, Host, Router
import json
import uvicorn

with open("config.json") as file:
    conf:dict[str, list[dict[str, str]]] = json.loads(file.read())
    for k,v in conf.items():
        conf[k].sort(key=lambda x: x["path"], reverse=True)

async def router(request: Request):
    path: str = "/"+request.path_params["path"]
    host = request.path_params["host"]
    result = conf

    for route in conf.get(host):
        if path.startswith(route["path"]):
            result = f"Redirected to {route["service"]}"
            break

    return Response(f"path: {path} \nHost: {host}\nresult: {result}")


routes=[
    Route("/{path:path}", router)
    ]
routes = Router(routes)
routes = [
    Host('{host}', routes, name="site_api")
]
app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    print(conf)
    uvicorn.run("server:app", host="127.0.0.1", port=8000, log_level="info")

