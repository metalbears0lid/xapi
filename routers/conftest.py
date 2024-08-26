import os
from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from xapi.routers.post import comment_table, post_table

os.environ['ENV_STATE'] = 'test'

from xapi.main import app   # noqa:E402


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'

@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)

@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    post_table.clear()
    comment_table.clear()
    yield