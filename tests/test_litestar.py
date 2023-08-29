from contextlib import asynccontextmanager
from functools import partial

import pytest
from asyncpg import Connection
from litestar import Litestar, get
from litestar.testing import create_test_client
from server.app.contrib.asyncpg import AsyncpgConfig, AsyncpgPlugin, PoolConfig


@pytest.mark.asyncio
async def test_l():
    @get("/")
    async def health_check(provide_connection: Connection) -> float:
        """Check database available and returns random number."""
        r = await provide_connection.fetch("select random()")
        return r[0]["random"]

    @asynccontextmanager
    async def lifespan(_app: Litestar):
        print(1)  # noqa: T201
        yield
        print(2)  # noqa: T201

    asyncpg_config = AsyncpgConfig(pool_config=PoolConfig(dsn="postgresql://postgres:postgres@localhost:5432/postgres"))
    asyncpg = AsyncpgPlugin(config=asyncpg_config)
    with create_test_client(route_handlers=[health_check], plugins=[asyncpg], lifespan=[partial(lifespan)]) as client:
        response = client.get("/")
        assert response.status_code == 200
