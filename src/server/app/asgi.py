# pylint: disable=[invalid-name,import-outside-toplevel]
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from litestar import Litestar


def create_app() -> Litestar:
    """Create ASGI application."""

    from litestar import Litestar

    from app import domain

    return Litestar(
        plugins=[
            domain.plugins.socketify,
            domain.plugins.asyncpg,
            domain.plugins.aiosql,
        ],
    )
