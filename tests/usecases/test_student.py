"""Student usecases test module."""

from src.usecases.student import StudentUsecase
from src.schemas.student import StudentOut

student_usecase = StudentUsecase()


async def test_create_student(student_in):
    """Test create student usecase."""

    student = await student_usecase.create(body=student_in)
    assert isinstance(student, StudentOut)
