from litestar_asyncpg import AsyncpgConfig, AsyncpgPlugin, PoolConfig
from litestar_granian import GranianPlugin

asyncpg = AsyncpgPlugin(config=AsyncpgConfig(pool_config=PoolConfig(dsn="postgresql://app:app@localhost:5432/app")))
granian = GranianPlugin()
