from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel


class GetCurso(CamelModel):
    id: int
    titulo: str
    descricao: str
    carga_horaria: int
    qtd_exercicios: int

    class Config:
        orm_mode = True


class PostCurso(CamelModel):
    titulo: str
    descricao: str
    carga_horaria: int
    qtd_exercicios: int


class UpdateCurso(CamelModel):
    titulo: str
    descricao: str
    carga_horaria: int
    qtd_exercicios: int

