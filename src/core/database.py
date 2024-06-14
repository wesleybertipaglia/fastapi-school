"""Database module."""

from motor.motor_asyncio import AsyncIOMotorClient
from src.core.settings import Settings

settings = Settings()


class MongoClient:
    """MongoDB client class."""

    def __init__(self):
        self.client = AsyncIOMotorClient(settings.DATABASE_URL)

    def get(self) -> AsyncIOMotorClient:
        """Get mongo client."""

        return self.client

    def close(self):
        """Close mongo client."""

        self.client.close()
