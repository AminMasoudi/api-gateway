#! python

import uvicorn, os


def main():
    os.environ.setdefault("SETTINGS", "settings.dev")
    from utils import settings
    uvicorn.run(app="server:admin_app", port=settings.ADMIN_PORT, reload=True)

if __name__ == "__main__":
    main()