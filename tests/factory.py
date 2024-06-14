"""Factory for schemas to generate random data for testing"""

from faker import Faker

from src.schemas.alumni import AlumniIn

faker = Faker()


def alumni_factory():
    return AlumniIn(
        name=faker.name(),
        email=faker.email(),
        phone=faker.phone_number(),
        address=faker.address(),
        birthdate=faker.date_of_birth(),
        gender=faker.random_element(elements=("M", "F")),
    )
