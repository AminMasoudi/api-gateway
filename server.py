from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route, Host, Router
from utils import settings as config
import httpx, requests
import json

routing_hosts = config.routing_hosts



async def router(request: Request):

    path: str = "/" + request.path_params["path"]
    host = request.path_params["host"]
    result = ""

    for route in routing_hosts.get(host):
        if path.startswith(route["path"]):
            result = "http://"+ route["service"] + path
            break
    try:
        response = httpx.request(
            method=request.method,
            url=result,
            # headers=request.headers
            )
    except Exception as e:
        print(e)
    
    return Response(
        content=response.content,
        status_code=response.status_code,
        )


routes = [Route("/{path:path}", router, methods=["POST", "GET"])]
routes = Router(routes)
routes = [Host("{host}", routes, name="site_api")]
app = Starlette(debug=True, routes=routes)
