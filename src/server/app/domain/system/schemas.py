from typing import Literal

import msgspec

__all__ = ["SystemHealth"]


class SystemHealth(msgspec.Struct, rename="camel"):
    """Health check response schema."""

    database_status: Literal["online", "offline"]
