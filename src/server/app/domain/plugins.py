from litestar_asyncpg import AsyncpgConfig, AsyncpgPlugin, PoolConfig

from app.contrib.aiosql.plugin import AioSQLConfig, AioSQLPlugin

asyncpg = AsyncpgPlugin(config=AsyncpgConfig(pool_config=PoolConfig(dsn="postgresql://app:app@localhost:5432/app")))
aiosql = AioSQLPlugin(config=AioSQLConfig())
