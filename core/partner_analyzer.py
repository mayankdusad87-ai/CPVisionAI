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
