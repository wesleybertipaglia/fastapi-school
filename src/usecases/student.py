"""Student usecase module."""

from typing import List
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from src.core.database import client
from src.schemas.student import StudentIn, StudentOut


class StudentUsecase:
    """Student usecase class."""

    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("students")

    async def create(self, body: StudentIn) -> StudentOut:
        """Create a student."""
        insert_result = await self.collection.insert_one(body.model_dump())
        inserted_id = insert_result.inserted_id
        inserted_document = await self.collection.find_one({"_id": inserted_id})
        student_out_data = {
            "id": str(inserted_document["_id"]),
            "created_at": inserted_document["created_at"],
            "updated_at": inserted_document["updated_at"],
        }
        return StudentOut(**student_out_data)

    async def list(self) -> List[StudentOut]:
        """List students."""
        return [StudentOut(**item) async for item in self.collection.find()]
