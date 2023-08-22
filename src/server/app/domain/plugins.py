from app.contrib.aiosql.plugin import AioSQLConfig, AioSQLPlugin
from app.contrib.asyncpg import AsyncpgConfig, AsyncpgPlugin, PoolConfig
from app.contrib.socketify import SocketifyPlugin

asyncpg_config = AsyncpgConfig(pool_config=PoolConfig(dsn="postgresql://app:app@localhost:5432/app"))
asyncpg_config.create_pool()
asyncpg = AsyncpgPlugin(config=asyncpg_config)

socketify = SocketifyPlugin()
aiosql = AioSQLPlugin(config=AioSQLConfig())
