from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route, Host, Router
import json
async def router(request: Request):
    path = request.path_params["path"]
    host = request.path_params["host"]
    return Response(f"path: {path} \nHost: {host}")
routes=[
    Route("/{path:path}", router)
    ]
routes = Router(routes)
routes = [
    Host('{host}', routes, name="site_api")
]
app = Starlette(debug=True, routes=routes)

