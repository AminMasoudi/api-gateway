from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route
import json

async def router(request: Request):
    path = request.path_params["path"]
    return Response(path)

app = Starlette(debug=True, routes=[
    Route("/{path:path}", router)
    ])