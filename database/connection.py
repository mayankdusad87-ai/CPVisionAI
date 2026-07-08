"""
=========================================================
ChannelIQ AI

Database Connection

Handles SQLite database connection.

=========================================================
"""

from __future__ import annotations

import sqlite3

from config import DB_PATH


class DatabaseConnection:
    """
    SQLite database connection manager.
    """

    def __init__(self):

        self.db_path = DB_PATH

    # --------------------------------------------------

    def connect(self) -> sqlite3.Connection:
        """
        Returns a SQLite connection.
        """

        return sqlite3.connect(self.db_path)

    # --------------------------------------------------

    def execute(
        self,
        query: str,
        params: tuple = (),
    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(query, params)

        conn.commit()

        conn.close()

    # --------------------------------------------------

    def fetch_all(
        self,
        query: str,
        params: tuple = (),
    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(query, params)

        rows = cursor.fetchall()

        conn.close()

        return rows

    # --------------------------------------------------

    def fetch_one(
        self,
        query: str,
        params: tuple = (),
    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(query, params)

        row = cursor.fetchone()

        conn.close()

        return row
