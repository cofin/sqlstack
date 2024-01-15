# pylint: disable=[invalid-name,import-outside-toplevel]
from __future__ import annotations

from typing import TYPE_CHECKING

__all__ = ["create_app"]


if TYPE_CHECKING:
    from litestar import Litestar


def create_app() -> Litestar:
    """Create ASGI application."""

    from litestar import Litestar

    from app.domain import plugins
    from app.domain.system.controllers import SystemController

    return Litestar(
        route_handlers=[SystemController],
        plugins=[plugins.asyncpg, plugins.granian],
    )
