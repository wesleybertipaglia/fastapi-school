"""Test settings module."""

import asyncio
import pytest
from src.core.database import MongoClient
from src.schemas.student import StudentIn
from tests.factories.student import student_factory

client = MongoClient()


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the session."""

    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    """Get a mongo client instance."""

    return client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    """Clear all collections in the database."""

    yield
    collection_names = await mongo_client.get_database().list_collection_names()
    for collection_name in collection_names:
        if collection_name.startswith("system"):
            continue

        await mongo_client.get_database()[collection_name].delete_many({})


@pytest.fixture(autouse=True)
def student_in():
    """Get a student_in instance."""

    data = student_factory()
    return StudentIn(**data.model_dump())
