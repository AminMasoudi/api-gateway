from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route, Host, Router

from utils import settings as config
from utils.routing import router as routing_func

client = config.call_client


async def router(request: Request):

    path: str = "/" + request.path_params["path"]
    host = request.path_params["host"]
    # routing

    # FIXME: specify the protocol to call that backend 
    service = routing_func(path=path, domain=host)              #<===== routing_func is a dependency
    print(service)
    # call a service
    content, code = await client.send_request(                  #<==== client is a dependency
        path=path,
        service=service,
        method=request.method,
    )

    return Response(content=content, status_code=code)


routes = [
    Route("/{path:path}", router, methods=["POST", "GET"]),
    ]

routes = Router(routes)
routes = [Host("{host}", routes, name="site_api")]

app = Starlette(
    debug=True,
    routes=routes
    )
