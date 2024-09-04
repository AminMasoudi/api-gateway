#! python
import os
import uvicorn


def main():
    os.environ.setdefault("SETTINGS", "settings.dev")
    from utils import settings

    uvicorn.run(
            app="server:app", 
            port=settings.PORT, 
            reload=settings.RELOAD if settings.RELOAD is not None else True, 
            host="0.0.0.0",
            workers=settings.WORKERS or 1
            )



if __name__ == "__main__":
    # [ ] load_config
    # [ ] preprocessing config files
    #   [ ] sorts and stuff like that
    # [ ] setup logger
    # [ ] start listening
    main()
