from fastapi import FastAPI
from contextlib import asynccontextmanager

from .src.db.db import init_database, close_database
from .src.routes.teams_routes import teams_router
from .src.routes.users_routes import users_router

import logging

# Logger config (Should prob be moved to it's own file since it's ugly as fuck)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# FastAPI Lifespan Method for startup and cleanup
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("--# Initializing database #--")
    init_database()
    logger.info("--# Database initialized #--")

    # TODO: Main App Logic Here ;P

    yield

    logger.info("--# Closing database #--")
    close_database()
    logger.info("--# Closed database #--")


# Create our app instance
app = FastAPI(lifespan=lifespan)

# Setup all API routes
app.include_router(teams_router)
app.include_router(users_router)
