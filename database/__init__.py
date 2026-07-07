"""
=========================================================
ChannelIQ AI
Database Package

This package provides all database functionality.

Usage:
    from database import DatabaseConnection
    from database import DatabaseRepository
    from database import create_tables
=========================================================
"""

from .connection import DatabaseConnection
from .repository import DatabaseRepository
from .models import create_tables

__all__ = [
    "DatabaseConnection",
    "DatabaseRepository",
    "create_tables",
]
