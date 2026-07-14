"""
=========================================================
ChannelIQ AI

Context Builder

Builds a structured AI context from the
AnalysisResult object.

This class NEVER performs calculations.

It simply converts verified business facts
into a format consumable by the AI layer.

=========================================================
"""

from __future__ import annotations

from typing import Any

from core.analysis_result import AnalysisResult


class ContextBuilder:
    """
    Converts AnalysisResult into an AI-ready context.

    AI should NEVER receive raw Excel data.

    AI should ONLY receive verified facts.
    """

    def build(
        self,
        result: AnalysisResult,
    ) -> dict[str, Any]:

        metadata = result.metadata or {}

        context = {

            # =====================================================
            # COMPANY
            # =====================================================

            "company": {

                "name": result.company_name,

                "project": result.project_name,

                "reporting_period": metadata.get(
                    "reporting_period",
                    "",
                ),

            },

            # =====================================================
            # EXECUTIVE KPI
            # =====================================================

            "business_snapshot": {

                "total_walkins":
                    metadata.get(
                        "total_walkins",
                        0,
                    ),

                "fresh_walkins":
                    metadata.get(
                        "fresh_walkins",
                        0,
                    ),

                "unique_revisits":
                    metadata.get(
                        "unique_revisits",
                        0,
                    ),

                "bookings":
                    result.total_bookings,

                "conversion":
                    result.conversion,

                "participating_cp":
                    metadata.get(
                        "participating_cp",
                        0,
                    ),

            },

            # =====================================================
            # TABLES
            # =====================================================

            "partner_intelligence":

                metadata.get(
                    "partner_summary",
                    {},
                ),

            "customer_intelligence":

                metadata.get(
                    "customer_journey",
                    {},
                ),

            "booking_intelligence":

                metadata.get(
                    "booking_summary",
                    {},
                ),

            # =====================================================
            # EXISTING AI
            # =====================================================

            

        return context

    # =====================================================
    # DEBUG
    # =====================================================

    def pretty_print(
        self,
        context: dict,
    ) -> None:

        import json

        print(

            json.dumps(

                context,

                indent=4,

                default=str,

            )

        )
# =====================================================
# EXECUTIVE CONTEXT
# =====================================================

"executive_context": {

    "analysis_id": result.analysis_id,

    "analysis_date": metadata.get(
        "generated_at",
        "",
    ),

},
