from app.modules.curso import repository, schema


class GetOneCursoUseCase:
    def __init__(self, id: int):
        self._repository = repository.CursoRepository()
        self._id = id

    async def execute(self):
        cursos = await self._repository.get_by_id(self._id)
        return schema.GetCurso.from_orm(cursos)
