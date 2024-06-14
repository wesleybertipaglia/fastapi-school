"""Test cases for Alumni schema"""

from pydantic import ValidationError
import pytest
from src.schemas.alumni import AlumniIn
from .factory import alumni_factory


def test_alumni_valid():
    data = alumni_factory()
    AlumniIn.model_validate(data)


def test_alumni_invalid():
    data = {
        "name": "Anakin Skywalker",
        "email": "anakin_skywalker@berkeley.edu",
        "phone": "123-456-7890",
        "address": "1234 Main St, Berkeley, CA 94704",
        "birthdate": "1990-01-01",
    }
    with pytest.raises(ValidationError) as e:
        AlumniIn.model_validate(data)

    assert e.value.errors()[0] == {
        "type": "missing",
        "loc": ("gender",),
        "msg": "Field required",
        "input": {
            "name": "Anakin Skywalker",
            "email": "anakin_skywalker@berkeley.edu",
            "phone": "123-456-7890",
            "address": "1234 Main St, Berkeley, CA 94704",
            "birthdate": "1990-01-01",
        },
        "url": "https://errors.pydantic.dev/2.7/v/missing",
    }
