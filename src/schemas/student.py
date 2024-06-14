"""Student schema module."""

from datetime import datetime
from pydantic import Field
from .base import BaseSchema


class StudentIn(BaseSchema):
    """Student schema for input data."""

    name: str = Field(..., description="Name.", min_length=1, max_length=255)
    email: str = Field(..., description="E-mail.", min_length=1, max_length=255)
    phone: str = Field(..., description="Phone number.", min_length=1, max_length=255)
    address: str = Field(..., description="Address.", min_length=1, max_length=255)
    birthdate: datetime = Field(..., description="Birthdate.")
    gender: str = Field(..., description="Gender (M/F).", min_length=1, max_length=1)


class StudentOut(BaseSchema):
    """Student schema for output data."""

    id: str = Field(..., description="Student ID.", min_length=1, max_length=255)
    created_at: datetime = Field(..., description="Creation date.")
    updated_at: datetime = Field(..., description="Update date.")
