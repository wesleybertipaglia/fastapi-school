from fastapi import FastAPI, APIRouter
from src.core.settings import Settings
from src.routes.student import StudentRouter

api_router = APIRouter()
settings = Settings()
student_router = StudentRouter()


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
api_router.include_router(student_router, prefix="/students")
