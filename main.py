import sys

sys.path.append('..')

from contextlib import asynccontextmanager
from fastapi import FastAPI

from xapi.database import database
from xapi.routers.post import router as post_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()    # setup
    yield                       # wait for fastapi to tell contextmanager to continue
    await database.disconnect() # teardown

app = FastAPI(lifespan=lifespan)

app.include_router(post_router)

