"""Student router module"""

from typing import List
from fastapi import APIRouter, Depends, status

from src.schemas.student import StudentOut
from src.usecases.student import StudentUsecase

router = APIRouter(tags=["products"])


@router.get(path="/", status_code=status.HTTP_200_OK)
async def list(usecase: StudentUsecase = Depends()) -> List[StudentOut]:
    return await usecase.list()
