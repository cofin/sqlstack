from app.contrib.aiosql.plugin import AioSQLConfig, AioSQLPlugin
from app.contrib.asyncpg import AsyncpgConfig, AsyncpgPlugin, PoolConfig
from app.contrib.socketify import SocketifyPlugin

asyncpg = AsyncpgPlugin(config=AsyncpgConfig(pool_config=PoolConfig(dsn="postgresql://app:app@localhost:5432/app")))

socketify = SocketifyPlugin()
aiosql = AioSQLPlugin(config=AioSQLConfig())
