from loguru import logger

from app.config.bootstrap import create_app
from app.config.db import close_connection_database, connect_to_database
from app.config.middlewares import init_middlewares
from app.config.routers import init_routers

app = create_app()

init_middlewares(app)


@app.on_event("startup")
async def statup_event():
    logger.info("Starting database...")
    await connect_to_database()


@app.on_event("startup")
async def statup_routers():
    logger.info("Starting routers...")
    await init_routers(app)


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    await close_connection_database()
