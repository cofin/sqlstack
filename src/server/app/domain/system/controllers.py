from __future__ import annotations

from typing import TYPE_CHECKING, Literal, TypeVar

from litestar import Controller, MediaType, get
from litestar.response import Response

from app.domain.system import schemas

if TYPE_CHECKING:
    from asyncpg import Connection

    pass


OnlineOffline = TypeVar("OnlineOffline", bound=Literal["online", "offline"])


class SystemController(Controller):
    tags = ["System"]

    @get(
        operation_id="SystemHealth",
        name="system:health",
        path="/health",
        media_type=MediaType.JSON,
        cache=False,
        summary="Health Check",
        description="Execute a health check against backend components.  Returns system information including database and cache status.",
    )
    async def health_check(self, db_connection: Connection) -> Response[schemas.SystemHealth]:
        """Check database available and returns app config info."""
        try:
            await db_connection.fetch("select 1")
            db_ping = True
        except ConnectionRefusedError:
            db_ping = False

        healthy = bool(db_ping)

        return Response(
            content=schemas.SystemHealth(database_status="online" if db_ping else "offline"),
            status_code=200 if healthy else 500,
            media_type=MediaType.JSON,
        )
