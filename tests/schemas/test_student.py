"""Student schemas test module."""

import pytest
from pydantic import ValidationError
from src.schemas.student import StudentIn
from tests.factories.student import student_factory


def test_valid_student():
    """Test student schema with valid data."""

    data = student_factory()
    StudentIn.model_validate(data)


def test_invalid_student():
    """Test student schema with invalid data."""

    data = student_factory()

    with pytest.raises(ValidationError) as e:
        StudentIn.model_validate(data)

    assert e.value.errors()[0]["type"] == "missing"
    assert e.value.errors()[0]["msg"] == "Field required"
