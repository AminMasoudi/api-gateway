
from starlette.requests import Request
from starlette.responses import Response
from starlette.applications import Starlette
from starlette_admin.contrib.sqla import Admin, ModelView

from app import App, Depends
from dependencies import get_call_client, get_db
from model.models import Backend
from utils.setting import settings
from utils.routing import find_service
from utils.http_client import AbstractClient


app = App(debug=True)

admin_app = Starlette()  # or app = FastAPI()
admin = Admin(get_db(), title="Admin", base_url="/api-admin")
admin.add_view(ModelView(Backend, icon="fas fa-server"))
admin.mount_to(admin_app)


@app.route(
        path="/{path:path}",
        methods=["GET", "POST", "HEAD", "DELETE"]
        )
async def router(request: Request,
                url_maps: dict=Depends(settings.get_url_maps),
                call_client:AbstractClient=Depends(get_call_client)
                ):

    path: str = "/" + request.path_params["path"]
    host = request.path_params["host"]

    # routing
    # FIXME: specify the protocol to call that backend
    service = find_service(maps=url_maps, path=path, domain=host)

    # call a service
    content, code = await call_client.send_request(
        path=path,
        service=service,
        method=request.method,
    )
    return Response(content=content, status_code=code)


