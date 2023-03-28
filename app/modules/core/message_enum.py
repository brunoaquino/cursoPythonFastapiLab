from enum import Enum


class MessageEnum(Enum):
    """
    Enum for message types.
    """

    CURSO_NOT_FOUND = "Curso not found"
    CURSO_ALREADY_EXISTS = "Curso already exists"
    CURSO_NOT_UPDATED = "Curso not updated"
    