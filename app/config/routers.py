from fastapi import FastAPI
from fastapi_pagination import add_pagination


async def init_routers(app: FastAPI):
    """
    This function is to load all routers in application.
    Here you can add routers from your modules.
    :param app:
    :return:
    """
    from app.modules.curso import router as curso_router
    from app.modules.core import helthcheck_router

    app.include_router(helthcheck_router.router)
    app.include_router(
        curso_router.router, prefix="/curso", tags=["Curso"]
    )
    add_pagination(app)
