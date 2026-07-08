"""
=========================================================
ChannelIQ AI

Database Repository

Responsible for all database CRUD operations.

=========================================================
"""

from __future__ import annotations

from database.connection import DatabaseConnection
from core.analysis_result import AnalysisResult


class DatabaseRepository:

    """
    Repository layer for Analysis History.
    """

    def __init__(self):

        self.db = DatabaseConnection()

    # =====================================================
    # SAVE ANALYSIS
    # =====================================================

    def save_analysis(
        self,
        result: AnalysisResult,
    ) -> None:

        query = """
        INSERT INTO analysis_history (

            analysis_id,

            company_name,

            project_name,

            month,

            year,

            fresh_walkins,

            unique_revisits,

            bookings,

            booking_percentage,

            active_channel_partners,

            health_score,

            revenue_opportunity,

            growth_rate,

            ai_summary

        )

        VALUES (

            ?,?,?,?,?,?,?,?,?,?,?,?,?,?

        )
        """

        metadata = result.metadata or {}

        self.db.execute(

            query,

            (

                result.analysis_id,

                result.company_name,

                result.project_name,

                result.month,

                result.year,

                metadata.get("fresh_walkins", 0),

                metadata.get("unique_revisits", 0),

                result.total_bookings,

                result.conversion,

                metadata.get("active_channel_partners", 0),

                result.health_score,

                result.revenue_opportunity,

                result.growth_rate,

                getattr(result, "ai_summary", "")

            )

        )

    # =====================================================
    # GET ALL HISTORY
    # =====================================================

    def get_history(self):

        query = """

        SELECT *

        FROM analysis_history

        ORDER BY created_at DESC

        """

        return self.db.fetch_all(query)

    # =====================================================
    # GET BY ANALYSIS ID
    # =====================================================

    def get_analysis(

        self,

        analysis_id: str,

    ):

        query = """

        SELECT *

        FROM analysis_history

        WHERE analysis_id = ?

        """

        return self.db.fetch_one(

            query,

            (analysis_id,)

        )

    # =====================================================
    # GET LATEST ANALYSIS
    # =====================================================

    def latest_analysis(self):

        query = """

        SELECT *

        FROM analysis_history

        ORDER BY created_at DESC

        LIMIT 1

        """

        return self.db.fetch_one(query)

    # =====================================================
    # DELETE ANALYSIS
    # =====================================================

    def delete_analysis(

        self,

        analysis_id: str,

    ) -> None:

        query = """

        DELETE FROM analysis_history

        WHERE analysis_id = ?

        """

        self.db.execute(

            query,

            (analysis_id,)

        )

    # =====================================================
    # DELETE ALL HISTORY
    # =====================================================

    def clear_history(self) -> None:

        self.db.execute(

            "DELETE FROM analysis_history"

        )

    # =====================================================
    # TOTAL ANALYSIS COUNT
    # =====================================================

    def total_analyses(self) -> int:

        row = self.db.fetch_one(

            """

            SELECT COUNT(*)

            FROM analysis_history

            """

        )

        if row is None:

            return 0

        return int(row[0])
