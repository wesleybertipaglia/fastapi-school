"""Settings module."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings class."""

    PROJECT_NAME: str = "School Management System"
    VERSION: str = "0.1.0"
    ROOT_DIR: str = "/"
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env")
