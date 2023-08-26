from typing import Literal

import msgspec


class SystemHealth(msgspec.Struct, rename="camel"):
    """Health check response schema."""

    database_status: Literal["online", "offline"]
