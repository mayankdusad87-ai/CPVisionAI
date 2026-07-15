"""
=========================================================
ChannelIQ AI

Findings Engine

Generates verified business findings from
AnalysisResult.

No AI.
No OpenAI.

Only business observations.

=========================================================
"""

from __future__ import annotations

from typing import Any


class FindingsEngine:
    """
    Creates business findings that can later
    be explained by AI.
    """

    # =====================================================
    # PUBLIC
    # =====================================================

    def analyse(
        self,
        context: dict[str, Any],
    ) -> dict[str, list]:

        findings = []

        risks = []

        opportunities = []

        business_snapshot = context["business_snapshot"]

        partner_summary = context.get(
            "partner_intelligence",
            {},
        )
        commercial = context.get(
           "commercial_intelligence",
           {},
       )

        # -----------------------------------------------
        # KPI Findings
        # -----------------------------------------------

        findings.extend(

            self.dashboard_findings(
                business_snapshot
            )

        )

        # -----------------------------------------------
        # Partner Findings
        # -----------------------------------------------

        if isinstance(partner_summary, dict):

            findings.extend(

                self.partner_findings(
                    partner_summary
                )

            )

        # -----------------------------------------------

        for item in findings:

            if item["type"] == "Risk":

                risks.append(item)

            elif item["type"] == "Opportunity":

                opportunities.append(item)

        return {

            "findings": findings,

            "risks": risks,

            "opportunities": opportunities,

        }

    # =====================================================
    # DASHBOARD FINDINGS
    # =====================================================

    def dashboard_findings(
        self,
        dashboard: dict,
    ) -> list:

        findings = []

        fresh = dashboard.get(
            "fresh_walkins",
            0,
        )

        bookings = dashboard.get(
            "bookings",
            0,
        )

        conversion = dashboard.get(
            "conversion",
            0,
        )

        participating = dashboard.get(
            "participating_cp",
            0,
        )

        # -----------------------------------------------

        findings.append(

            {

                "title":
                    "Fresh Walk-ins",

                "type":
                    "Observation",

                "priority":
                    "Medium",

                "message":

                    f"The business generated "
                    f"{fresh} fresh walk-ins.",

            }

        )

        # -----------------------------------------------

        findings.append(

            {

                "title":
                    "Bookings",

                "type":
                    "Observation",

                "priority":
                    "Medium",

                "message":

                    f"{bookings} bookings "
                    f"were recorded.",

            }

        )

        # -----------------------------------------------

        if conversion < 5:

            findings.append(

                {

                    "title":
                        "Low Conversion",

                    "type":
                        "Risk",

                    "priority":
                        "High",

                    "message":

                        f"Overall booking conversion "
                        f"is only {conversion:.2f}%."

                }

            )

        elif conversion >= 10:

            findings.append(

                {

                    "title":
                        "Healthy Conversion",

                    "type":
                        "Opportunity",

                    "priority":
                        "High",

                    "message":

                        f"Overall conversion "
                        f"is {conversion:.2f}%."

                }

            )

        # -----------------------------------------------

        findings.append(

            {

                "title":
                    "Partner Network",

                "type":
                    "Observation",

                "priority":
                    "Low",

                "message":

                    f"{participating} channel "
                    f"partners participated "
                    f"during this period.",

            }

        )

        return findings

    # =====================================================
    # PARTNER FINDINGS
    # =====================================================

    def partner_findings(
        self,
        partner_summary: dict,
    ) -> list:

        findings = []

        summary = partner_summary.get(
            "summary",
            None,
        )

        if summary is None:

            return findings

        if len(summary) == 0:

            return findings

        # -----------------------------------------------

        top_conversion = summary.sort_values(

            by="conversion",

            ascending=False,

        ).iloc[0]

        findings.append(

            {

                "title":
                    "Best Partner",

                "type":
                    "Opportunity",

                "priority":
                    "High",

                "message":

                    f"{top_conversion['partner']} "
                    f"has the highest booking "
                    f"conversion of "
                    f"{top_conversion['conversion']}%."

            }

        )

        # -----------------------------------------------

        top_walkins = summary.sort_values(

            by="fresh_walkins",

            ascending=False,

        ).iloc[0]

        findings.append(

            {

                "title":
                    "Highest Lead Generator",

                "type":
                    "Observation",

                "priority":
                    "Medium",

                "message":

                    f"{top_walkins['partner']} "
                    f"generated the highest "
                    f"fresh walk-ins."

            }

        )

        # -----------------------------------------------

        low_conversion = summary[

            (summary["fresh_walkins"] >= 10)

            &

            (summary["conversion"] < 5)

        ]

        if not low_conversion.empty:

            findings.append(

                {

                    "title":
                        "High Volume Low Conversion",

                    "type":
                        "Risk",

                    "priority":
                        "High",

                    "message":

                        f"{len(low_conversion)} "
                        f"partners generated "
                        f"good lead volume "
                        f"but poor conversion."

                }

            )

        return findings

    # =====================================================
    # PRIORITIZE
    # =====================================================

    def prioritize(
        self,
        findings: list,
    ) -> list:

        priority = {

            "High": 1,

            "Medium": 2,

            "Low": 3,

        }

        return sorted(

            findings,

            key=lambda x:

            priority.get(

                x["priority"],

                99,

            ),

        )
