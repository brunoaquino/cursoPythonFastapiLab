from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate
from starlette import status

from app.config.settings import get_settings

from ..core.logging import LoggingUnder
from . import schema
from . import usecase 

router = APIRouter()

settings = get_settings()


@router.post(
    "/",
    description="This router is to create new curso",
    status_code=status.HTTP_201_CREATED,
    response_model=schema.GetCurso,
    dependencies=[Depends(LoggingUnder())],
)
async def post_curso(payload: schema.PostCurso):
    return await usecase.CreateCursoUseCase(payload).execute()


@router.get(
    "/",
    description="Router to list all Cursos registered",
    response_model=Page[schema.GetCurso],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(LoggingUnder())],
)
async def get_all_cursos():
    cursos = await usecase.GetAllCursoUseCase().execute()
    return paginate(cursos)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    description="Router to one Curso by id",
    response_model=schema.GetCurso,
    dependencies=[Depends(LoggingUnder())],
)
async def get_curso(id: int):
    return await usecase.GetOneCursoUseCase(id).execute()


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(LoggingUnder())],
    description="Router to update Curso by id",
)
async def put_curso(id: int, payload: schema.UpdateCurso):
    return await usecase.UpdateCursoUseCase(id, payload).execute()
