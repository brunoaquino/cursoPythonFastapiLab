from fastapi import HTTPException, status

from app.modules.curso import repository, schema
from app.modules.core.message_enum import MessageEnum


class UpdateCursoUseCase:
    def __init__(self, id: int, payload: schema.UpdateCurso):
        self._repository = repository.CursoRepository()
        self._payload = payload
        self._id = id

    async def _validate(self):
        curso = await self._repository.get_by_id(self._id)
        if not curso:
            raise HTTPException(
                status_code=400, detail=MessageEnum.CURSO_NOT_FOUND.value
            )

        curso.carga_horaria = self._payload.carga_horaria
        curso.descricao = self._payload.descricao
        curso.qtd_exercicios = self._payload.qtd_exercicios
        curso.titulo = self._payload.titulo
        return curso

    async def execute(self):
        curso_entity = await self._validate()
        has_updated = await self._repository.update(curso_entity)
        if not has_updated:
            raise HTTPException(
                status_code=status.HTTP_501_NOT_IMPLEMENTED,
                detail=MessageEnum.CURSO_NOT_UPDATED.value,
            )
        return schema.GetCurso.from_orm(curso_entity)