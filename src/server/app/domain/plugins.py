from litestar_asyncpg import AsyncpgConfig, AsyncpgPlugin, PoolConfig

from app.contrib.aiosql.plugin import AioSQLConfig, AioSQLPlugin
from app.contrib.socketify import SocketifyPlugin

asyncpg = AsyncpgPlugin(config=AsyncpgConfig(pool_config=PoolConfig(dsn="postgresql://app:app@localhost:5432/app")))
socketify = SocketifyPlugin()
aiosql = AioSQLPlugin(config=AioSQLConfig())
