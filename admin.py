#! python

from starlette.applications import Starlette
from starlette_admin.contrib.sqla import Admin, ModelView
import uvicorn, os

from model.models import Backend
from .dependencies import get_db

os.environ.setdefault("SETTINGS", "settings.dev")
from utils import settings

app = Starlette()  # or app = FastAPI()
admin = Admin(get_db(), title="Test", base_url="/api-admin")
admin.add_view(ModelView(Backend, icon="fas fa-server"))
admin.mount_to(app)

def main():
    uvicorn.run(app="admin:app", port=settings.ADMIN_PORT, reload=True)

if __name__ == "__main__":
    main()