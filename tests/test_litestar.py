from contextlib import asynccontextmanager
from functools import partial

import pytest
from litestar import Litestar, get, Request, Response
from litestar.testing import create_test_client
from asyncpg import Connection

from server.app.contrib.asyncpg import AsyncpgPlugin, AsyncpgConfig, PoolConfig


@pytest.mark.asyncio
async def test_l():
    @get("/")
    async def health_check(provide_connection: Connection) -> Response:
        """Check database available and returns app config info."""
        try:
            await provide_connection.fetch("select 1")
            db_ping = True
        except ConnectionRefusedError:
            db_ping = False

        healthy = bool(db_ping)

        return Response(
            status_code=200 if healthy else 500,
            content=healthy
        )

    @asynccontextmanager
    async def lifespan(_app: Litestar):
        print(1)
        yield
        print(2)

    asyncpg_config = AsyncpgConfig(pool_config=PoolConfig(dsn="postgresql://postgres:postgres@localhost:5432/postgres"))
    asyncpg = AsyncpgPlugin(config=asyncpg_config)
    with create_test_client(route_handlers=[health_check],
                            plugins=[asyncpg],
                            lifespan=[partial(lifespan)]
                            ) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() is True
