"""Alumni schema module."""

from datetime import datetime
from pydantic import Field
from .base import BaseSchema


class AlumniIn(BaseSchema):
    """Alumni schema for input data."""

    name: str = Field(..., description="Alumni name.", min_length=1, max_length=255)
    email: str = Field(..., description="Alumni email.", min_length=1, max_length=255)
    phone: str = Field(
        ..., description="Alumni phone number.", min_length=1, max_length=255
    )
    address: str = Field(
        ..., description="Alumni address.", min_length=1, max_length=255
    )
    birthdate: datetime = Field(..., description="Alumni birthdate.")
    gender: str = Field(
        ..., description="Alumni gender (M/F).", min_length=1, max_length=1
    )
