from app.modules.curso import repository, schema


class GetAllCursoUseCase:
    def __init__(self):
        self._repository = repository.CursoRepository()

    async def _serializer(self, curso):
        return schema.GetCurso.from_orm(curso)

    async def execute(self):
        cursos = await self._repository.get_all()
        return [await self._serializer(curso) for curso in cursos]
