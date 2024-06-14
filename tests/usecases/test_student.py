from src.usecases.student import student_usecase
from src.schemas.student import StudentOut


async def test_usecase_create_student(student_in):
    student = await student_usecase.create(body=student_in)
    assert isinstance(student, StudentOut)
