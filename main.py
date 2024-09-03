#! python
import os
import uvicorn


def main():
    os.environ.setdefault("SETTINGS", "settings.dev")
    from utils import settings

    uvicorn.run(app="server:app", port=settings.PORT, reload=True, host="0.0.0.0")



if __name__ == "__main__":
    # [ ] load_config
    # [ ] preprocessing config files
    #   [ ] sorts and stuff like that
    # [ ] setup logger
    # [ ] start listening
    main()
