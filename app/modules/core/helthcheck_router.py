from fastapi import APIRouter, Depends, Request

from app.modules.core.logging import LoggingSystem

router = APIRouter()


@router.get(
    "/health-check",
    description="Router to check helth application",
    dependencies=[Depends(LoggingSystem())],
)
async def helthcheck(_request: Request):
    return {"msg": "Application running"}
