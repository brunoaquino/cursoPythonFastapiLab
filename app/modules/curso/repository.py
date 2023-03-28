from tortoise.exceptions import BaseORMException

from app.modules.curso.model import Curso
from typing import Optional, Dict

class CursoRepository:
    def __init__(self):
        self.entity = Curso

    async def create(self, payload: dict) -> Curso:
        return await self.entity.create(**payload)

    async def update(self, payload: Curso) -> bool:
        try:
            await payload.save()
            return True
        except BaseORMException:
            return False

    async def get_all(self) -> list:
        return await self.entity.all()

    async def get_by_id(self, id: int) -> Optional[Dict]:
        return await self.entity.get_or_none(id=id)

    async def exists(self, titulo: str) -> bool:
        titulo_result = await self.entity.get_or_none(titulo=titulo)
        return titulo_result is not None
