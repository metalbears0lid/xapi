# fixtures are ways to share data between multiple tests

from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

from xapi.main import app
from xapi.routers.post import comment_table, post_table


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

# client will be evaluated via fixture and injected into the function (dependency injection)
@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(transport=ASGITransport(app=app), base_url=client.base_url) as ac:
        yield ac
