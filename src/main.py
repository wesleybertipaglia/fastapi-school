from fastapi import FastAPI
from .core.settings import settings


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            title=settings.PROJECT_NAME,
            version=settings.VERSION,
            root_path=settings.ROOT_DIR
        )


app = App()
