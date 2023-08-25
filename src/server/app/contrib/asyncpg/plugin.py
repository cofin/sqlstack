from __future__ import annotations

from typing import TYPE_CHECKING

from litestar.plugins import InitPluginProtocol

if TYPE_CHECKING:
    from litestar.config.app import AppConfig

    from .config import AsyncpgConfig


class SlotsBase:
    __slots__ = ("_config",)


class AsyncpgPlugin(InitPluginProtocol, SlotsBase):
    """Asyncpg plugin."""

    __slots__ = ()

    def __init__(self, config: AsyncpgConfig) -> None:
        """Initialize ``AsyncpgPlugin``.

        Args:
            config: configure and start Asyncpg.
        """
        self._config = config

    @property
    def config(self) -> AsyncpgConfig:
        """Return the plugin config.

        Returns:
            AsyncpgConfig.
        """
        return self._config

    def on_app_init(self, app_config: AppConfig) -> AppConfig:
        """Configure application for use with Asyncpg.

        Args:
            app_config: The :class:`AppConfig <.config.app.AppConfig>` instance.
        """
        app_config.before_send.append(self._config.before_send_handler)
        app_config.on_startup.insert(0, self._config.on_startup)
        app_config.on_shutdown.append(self._config.on_shutdown)
        app_config.signature_namespace.update(self._config.signature_namespace)
        return app_config
