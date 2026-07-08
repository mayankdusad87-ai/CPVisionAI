"""
=========================================================
ChannelIQ AI

Partner Analyzer

Analyses Channel Partner performance using
processed partner metrics.

Version : 1.0
=========================================================
"""

from __future__ import annotations

import pandas as pd


class PartnerAnalyzer:
    """
    Performs business analysis on
    Channel Partner performance.
    """

    def analyse(
        self,
        partner_df: pd.DataFrame,
    ) -> dict:

        if partner_df.empty:

            return {

                "summary": partner_df,

                "top_walkins": partner_df,

                "top_bookings": partner_df,

                "top_conversion": partner_df,

                "low_performing": partner_df,

                "active_count": 0,

                "recommendations": [],

            }

        summary = partner_df.copy()

        summary = summary.sort_values(

            by="fresh_walkins",

            ascending=False,

        ).reset_index(drop=True)

        summary["rank"] = (

            summary.index + 1

        )

        top_walkins = self.top_walkins(summary)

        top_bookings = self.top_bookings(summary)

        top_conversion = self.top_conversion(summary)

        low_performing = self.low_performing(summary)

        recommendations = self.generate_recommendations(

            summary,

            top_walkins,

            top_bookings,

            top_conversion,

            low_performing,

        )

        return {

            "summary": summary,

            "top_walkins": top_walkins,

            "top_bookings": top_bookings,

            "top_conversion": top_conversion,

            "low_performing": low_performing,

            "active_count": len(summary),

            "recommendations": recommendations,

        }

    # =====================================================
    # TOP PARTNERS
    # =====================================================

    def top_walkins(

        self,

        df: pd.DataFrame,

        top: int = 10,

    ) -> pd.DataFrame:

        return (

            df

            .sort_values(

                by="fresh_walkins",

                ascending=False,

            )

            .head(top)

        )

    # -----------------------------------------------------

    def top_bookings(

        self,

        df: pd.DataFrame,

        top: int = 10,

    ) -> pd.DataFrame:

        return (

            df

            .sort_values(

                by="bookings",

                ascending=False,

            )

            .head(top)

        )

    # -----------------------------------------------------

    def top_conversion(

        self,

        df: pd.DataFrame,

        top: int = 10,

    ) -> pd.DataFrame:

        return (

            df

            .sort_values(

                by="booking_percentage",

                ascending=False,

            )

            .head(top)

        )

    # =====================================================
    # LOW PERFORMING PARTNERS
    # =====================================================

    def low_performing(

        self,

        df: pd.DataFrame,

    ) -> pd.DataFrame:

        """
        Partners having

        Fresh Walk-ins >=10

        AND

        Booking % <5%
        """

        return df[

            (df["fresh_walkins"] >= 10)

            &

            (df["booking_percentage"] < 5)

        ].sort_values(

            by="fresh_walkins",

            ascending=False,

        )
            # =====================================================
    # BEST / WORST PARTNER
    # =====================================================

    def best_partner(
        self,
        df: pd.DataFrame,
    ) -> pd.Series | None:

        if df.empty:
            return None

        return df.sort_values(
            by="booking_percentage",
            ascending=False,
        ).iloc[0]

    # -----------------------------------------------------

    def worst_partner(
        self,
        df: pd.DataFrame,
    ) -> pd.Series | None:

        if df.empty:
            return None

        filtered = df[df["fresh_walkins"] >= 10]

        if filtered.empty:
            return None

        return filtered.sort_values(
            by="booking_percentage",
            ascending=True,
        ).iloc[0]

    # =====================================================
    # BUSINESS RECOMMENDATIONS
    # =====================================================

    def generate_recommendations(
        self,
        summary: pd.DataFrame,
        top_walkins: pd.DataFrame,
        top_bookings: pd.DataFrame,
        top_conversion: pd.DataFrame,
        low_performing: pd.DataFrame,
    ) -> list[str]:

        recommendations = []

        # ----------------------------------------------

        if not top_walkins.empty:

            row = top_walkins.iloc[0]

            recommendations.append(

                f"{row.iloc[0]} generated the highest "
                f"fresh walk-ins ({int(row['fresh_walkins'])}). "
                "Continue strengthening this relationship."

            )

        # ----------------------------------------------

        if not top_bookings.empty:

            row = top_bookings.iloc[0]

            recommendations.append(

                f"{row.iloc[0]} achieved the highest number "
                f"of bookings ({int(row['bookings'])}). "
                "Study and replicate this partner's approach."

            )

        # ----------------------------------------------

        if not top_conversion.empty:

            row = top_conversion.iloc[0]

            recommendations.append(

                f"{row.iloc[0]} has the best booking "
                f"conversion ({row['booking_percentage']}%). "
                "Use this partner as a benchmark."

            )

        # ----------------------------------------------

        if not low_performing.empty:

            recommendations.append(

                f"{len(low_performing)} partner(s) generated "
                "good walk-ins but poor conversion. "
                "Review follow-up quality and lead qualification."

            )

        return recommendations

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    def executive_summary(
        self,
        analysis: dict,
    ) -> str:

        active = analysis["active_count"]

        recommendations = analysis["recommendations"]

        text = (
            f"The network currently has "
            f"{active} active channel partners."
        )

        if recommendations:

            text += " " + recommendations[0]

        return text

    # =====================================================
    # COMPLETE REPORT
    # =====================================================

    def report(
        self,
        partner_df: pd.DataFrame,
    ) -> dict:

        analysis = self.analyse(partner_df)

        analysis["best_partner"] = self.best_partner(
            partner_df
        )

        analysis["worst_partner"] = self.worst_partner(
            partner_df
        )

        analysis["executive_summary"] = (

            self.executive_summary(

                analysis

            )

        )

        return analysis
