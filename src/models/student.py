"""Student model module."""

from src.models.base import BaseModel
from src.schemas.student import StudentIn


class Student(StudentIn, BaseModel):
    """Student model class."""

    ...
