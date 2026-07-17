"""
=========================================================
ChannelIQ AI

Context Builder
=========================================================
"""

from __future__ import annotations

from typing import Any

from core.analysis_result import AnalysisResult


class ContextBuilder:

    def build(
        self,
        result: AnalysisResult,
    ) -> dict[str, Any]:

        metadata = result.metadata or {}

        context = {

            # -------------------------------------------------
            # COMPANY
            # -------------------------------------------------

            "company": {

                "name": result.company_name,

                "project": result.project_name,

                "reporting_period": metadata.get(
                    "reporting_period",
                    "",
                ),

            },

            # -------------------------------------------------
            # EXECUTIVE CONTEXT
            # -------------------------------------------------

            "executive_context": {

                "analysis_id": result.analysis_id,

                "analysis_date": metadata.get(
                    "generated_at",
                    "",
                ),

            },

            # -------------------------------------------------
            # BUSINESS SNAPSHOT
            # -------------------------------------------------

            "business_snapshot": {

                "total_walkins": metadata.get(
                    "total_walkins",
                    0,
                ),

                "fresh_walkins": metadata.get(
                    "fresh_walkins",
                    0,
                ),

                "unique_revisits": metadata.get(
                    "unique_revisits",
                    0,
                ),

                "bookings": result.total_bookings,

                "conversion": result.conversion,

                "participating_cp": metadata.get(
                    "participating_cp",
                    0,
                ),

            },

            # -------------------------------------------------
            # BUSINESS INTELLIGENCE
            # -------------------------------------------------

            "partner_intelligence": {
            
                "active_count": partner.get(
                    "active_count",
                    0,
                ),
            
                "executive_summary": partner.get(
                    "executive_summary",
                    "",
                ),
            
                "recommendations": partner.get(
                    "recommendations",
                    [],
                ),
            
                "best_partner": (
                    partner.get("best_partner").to_dict()
                    if hasattr(
                        partner.get("best_partner"),
                        "to_dict",
                    )
                    else None
                ),
            
                "worst_partner": (
                    partner.get("worst_partner").to_dict()
                    if hasattr(
                        partner.get("worst_partner"),
                        "to_dict",
                    )
                    else None
                ),
            
                "top_walkins": (
                    partner.get("top_walkins")
                    .head(5)
                    .to_dict("records")
                    if hasattr(
                        partner.get("top_walkins"),
                        "to_dict",
                    )
                    else []
                ),
            
                "top_conversion": (
                    partner.get("top_conversion")
                    .head(5)
                    .to_dict("records")
                    if hasattr(
                        partner.get("top_conversion"),
                        "to_dict",
                    )
                    else []
                ),
            
            },

            "customer_intelligence": metadata.get(
                "customer_journey",
                {},
            ),

            "booking_intelligence": metadata.get(
                "booking_summary",
                {},
            ),
            
            "commercial_intelligence": result.metadata.get(
               "commercial_intelligence",
               {},
            ),    
        }

        import json
        # -------------------------------------------------
        # VERIFIED BUSINESS FACTS
        # -------------------------------------------------

        context["verified_business_facts"] = {

            "company": context["company"],

            "business_snapshot": context["business_snapshot"],

            "commercial_intelligence": context["commercial_intelligence"],

            "partner_intelligence": context["partner_intelligence"],

            "customer_intelligence": context["customer_intelligence"],

            "booking_intelligence": context["booking_intelligence"],

        }

        print("=" * 80)
        print("AI CONTEXT")
        print("=" * 80)

        print(
            json.dumps(
                context,
                indent=4,
                default=str,
            )
        )

        print("=" * 80)

        return context
        

    # -------------------------------------------------

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
        


