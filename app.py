from functools import wraps, lru_cache
import typing

from starlette.applications import Starlette, AppType, Middleware, BaseRoute
from starlette.types import ExceptionHandler, Lifespan
from starlette.routing import Route, Router, Host

from utils.setting import Settings


class Depends:
    def __init__(self, callable: typing.Callable):
        self.dependency = callable


class App(Starlette):
    def __init__(
        self: AppType,
        dependency: dict[typing.Callable, typing.Callable] = {},
        debug: bool = False,
        routes: typing.Sequence[BaseRoute] | None = None,
        middleware: typing.Sequence[Middleware] | None = None,
        exception_handlers: typing.Mapping[typing.Any, ExceptionHandler] | None = None,
        on_startup: typing.Sequence[typing.Callable[[], typing.Any]] | None = None,
        on_shutdown: typing.Sequence[typing.Callable[[], typing.Any]] | None = None,
        lifespan: Lifespan[AppType] | None = None,
    ) -> None:
        self.dependency = dependency
        if routes is None:
            routes = []
            routes = Router(routes)
            routes = [Host("{host}", routes, name="site_api")]

        super().__init__(
            debug,
            routes,
            middleware,
            exception_handlers,
            on_startup,
            on_shutdown,
            lifespan,
        )

    @lru_cache
    def replace_dependency(self, arg):
        if arg.dependency not in self.dependency:
            self.dependency[arg.dependency] = arg.dependency
        return self.dependency[arg.dependency]()

    def route(self, path: str, methods: list[str]):
        def foo(func: callable):
            @wraps(func)
            async def wraper(*args, **kwargs):
                if func.__defaults__ is not None:
                    func.__defaults__ = tuple(
                        map(
                            lambda x: (
                                self.replace_dependency(x)
                                if isinstance(x, Depends)
                                else x
                            ),
                            func.__defaults__,
                        )
                    )
                return await func(*args, **kwargs)

            self.routes[0].app.routes.append(Route(path, wraper, methods=methods))
            return wraper

        return foo
