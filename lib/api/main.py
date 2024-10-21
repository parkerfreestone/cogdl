from fastapi import FastAPI
from contextlib import asynccontextmanager

from .db.db import init_database, close_database
from .routes.teams_routes import teams_router

import logging
import sys

# Logger config (Should prob be moved to it's own file since it's ugly as fuck)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter("%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s")
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)

# FastAPI Lifespan Method for startup and cleanup
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('--# Initializing database #--')
    init_database()
    logger.info('--# Database initialized #--')

    # TODO: Main App Logic Here ;P
    
    yield

    logger.info('--# Closing database #--')
    close_database()
    logger.info('--# Closed database #--')

# Create our app instance
app = FastAPI(lifespan=lifespan)

# Setup all API routes
app.include_router(teams_router)
