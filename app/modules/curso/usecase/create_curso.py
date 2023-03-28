from fastapi import HTTPException, status

from app.modules.curso import repository, schema
from app.modules.core.message_enum import MessageEnum


class CreateCursoUseCase:
    def __init__(self, payload: schema.GetCurso):
        self._repository = repository.CursoRepository()
        self._payload = payload

    async def _validate(self):
        if await self._repository.exists(self._payload.titulo):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=MessageEnum.CURSO_ALREADY_EXISTS.value,
            )

    async def execute(self):
        await self._validate()
        curso = await self._repository.create(self._payload.dict())
        return schema.GetCurso.from_orm(curso)
