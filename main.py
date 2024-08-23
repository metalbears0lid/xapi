import sys

sys.path.append('..')

from fastapi import FastAPI

from xapi.routers.post import router as post_router

app = FastAPI()

app.include_router(post_router)


