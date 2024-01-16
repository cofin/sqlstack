from __future__ import annotations

import os
import sys
from pathlib import Path

__all__ = ("run_cli",)


def run_cli() -> None:
    """Application Entrypoint."""
    current_path = Path(__file__).parent.parent.resolve()
    sys.path.append(str(current_path))
    os.environ["LITESTAR_APP"] = "app.asgi:create_app"
    try:
        from litestar.__main__ import run_cli as litestar_run_cli
    except ImportError as exc:
        print(  # noqa: T201
            "💣 Could not load required libraries.  ",
            "Please check your installation and make sure you activated any necessary virtual environment",
        )
        print(exc)  # noqa: T201
        sys.exit(1)
    litestar_run_cli()


if __name__ == "__main__":
    run_cli()
