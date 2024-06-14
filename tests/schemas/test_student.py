"""Student schemas test module."""

import pytest
from pydantic import ValidationError
from src.schemas.student import StudentIn
from tests.factories.student import StudentFactory

student_factory = StudentFactory()


def test_valid_student_in():
    """Test student schema with valid data."""

    data = student_factory.generate_in()
    student = StudentIn(**data.model_dump())

    assert student.name == data.name
    assert student.email == data.email
    assert student.phone == data.phone
    assert student.address == data.address
    assert student.birthdate == data.birthdate


def test_valid_student_out():
    """Test student schema with valid data."""

    data = student_factory.generate_out()
    student = StudentIn(**data.model_dump())

    assert student.id == data.id
    assert student.created_at == data.created_at
    assert student.updated_at == data.updated_at


def test_valid_student_update():
    """Test student schema with valid data."""

    data = student_factory.generate_update()
    student = StudentIn(**data.model_dump())

    assert student.name == data.name
    assert student.email == data.email
    assert student.phone == data.phone
    assert student.address == data.address
    assert student.birthdate == data.birthdate


def test_valid_student_delete():
    """Test student schema with valid data."""

    data = student_factory.generate_delete()
    student = StudentIn(**data.model_dump())

    assert student.id == data.id
    assert student.created_at == data.created_at
    assert student.updated_at == data.updated_at


def test_invalid_student_in():
    """Test student schema with invalid data."""

    with pytest.raises(ValidationError):
        StudentIn(name="", email="", phone="", address="", birthdate="")

    with pytest.raises(ValidationError):
        StudentIn(name="a", email="a", phone="a", address="a", birthdate="a")


def test_invalid_student_out():
    """Test student schema with invalid data."""

    with pytest.raises(ValidationError):
        StudentIn(id="", created_at="", updated_at="")

    with pytest.raises(ValidationError):
        StudentIn(id="a", created_at="a", updated_at="a")


def test_invalid_student_update():
    """Test student schema with invalid data."""

    with pytest.raises(ValidationError):
        StudentIn(name="", email="", phone="", address="", birthdate="")

    with pytest.raises(ValidationError):
        StudentIn(name="a", email="a", phone="a", address="a", birthdate="a")


def test_invalid_student_delete():
    """Test student schema with invalid data."""

    with pytest.raises(ValidationError):
        StudentIn(id="", created_at="", updated_at="")

    with pytest.raises(ValidationError):
        StudentIn(id="a", created_at="a", updated_at="a")
