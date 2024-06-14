"""Main module."""

from fastapi import FastAPI, APIRouter
from src.core.settings import Settings
from src.routes.student import router as student_router

api_router = APIRouter()
settings = Settings()


class App(FastAPI):
    """Application class."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            title=settings.PROJECT_NAME,
            version=settings.VERSION,
            root_path=settings.ROOT_DIR
        )


app = App()
api_router.include_router(student_router, prefix="/students")
