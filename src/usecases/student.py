"""Student usecase module."""

from typing import List
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import pymongo
from src.core.database import MongoClient
from src.schemas.student import StudentIn, StudentOut
from src.core.exceptions import NotFoundException

client = MongoClient()


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

        data = {
            "id": str(inserted_document["_id"]),
            "created_at": inserted_document["created_at"],
            "updated_at": inserted_document["updated_at"],
        }

        return StudentOut(data)

    async def list(self) -> List[StudentOut]:
        """List students."""

        return [StudentOut(**item) async for item in self.collection.find()]

    async def get(self, student_id: str) -> StudentOut:
        """Get a student."""

        document = await self.collection.find_one({"id": student_id})

        if not document:
            raise NotFoundException(message="Student not found.")

        return StudentOut(**document)

    async def update(self, student_id: str, body: StudentIn) -> StudentOut:
        """Update a student."""

        result = await self.collection.find_one_and_update(
            filter={"id": student_id},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        return StudentOut(**result)

    async def delete(self, student_id: str) -> bool:
        """Delete a student."""

        student = await self.collection.find_one({"id": student_id})
        if not student:
            raise NotFoundException(message="Student not found.")

        result = await self.collection.delete_one({"id": student_id})

        return True if result.deleted_count > 0 else False
