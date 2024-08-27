from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route, Host, Router

from utils.setting import settings
from utils.routing import find_service


async def router(request: Request):
    """
        in this function we have two dependency: `find_service` and `settings`
        we can ignore `find_service`, but what about `settings`??
        i cant use `async def router(request: Request, settings=Depends(settings)):` like FastAPI
        soo
        we ignore this one for now :)))
    """
    
    path: str = "/" + request.path_params["path"]
    host = request.path_params["host"]
    # routing

    # FIXME: specify the protocol to call that backend 
    service = find_service(maps=settings.url_maps, path=path, domain=host)

    # call a service
    content, code = await settings.call_client.send_request(
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
