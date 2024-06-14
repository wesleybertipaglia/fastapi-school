"""Student Factory Module."""

from faker import Faker
from src.schemas.student import StudentIn

faker = Faker()


def student_factory():
    """Generate random data for testing."""

    data = {
        "name": faker.name(),
        "email": faker.email(),
        "phone": faker.phone_number(),
        "address": faker.address(),
        "birthdate": faker.date_of_birth(),
        "gender": faker.random_element(elements=("M", "F")),
    }
    return StudentIn(**data)
