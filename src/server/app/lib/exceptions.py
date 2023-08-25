"""Litestar-saqlalchemy exception types.

Also, defines functions that translate service and repository exceptions
into HTTP exceptions.
"""
from __future__ import annotations

__all__ = ["ApplicationError"]


class ApplicationError(Exception):
    """Base exception type for the lib's custom exception types."""
