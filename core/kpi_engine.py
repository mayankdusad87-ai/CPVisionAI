"""
=========================================================
ChannelIQ AI

KPI Engine

Version : 3.0

Single source of truth for all KPI calculations.
=========================================================
"""

from __future__ import annotations

import pandas as pd

from core.column_mapping import (
    SOURCE,
    CHANNEL_PARTNER,
    CUSTOMER_FRESH_REVISIT,
    BOOKING_DONE,
    BUSINESS_VALUES,
)


class KPIEngine:

    """
    Calculates all Reporting KPIs.

    Business Rule:
    Every KPI is calculated ONLY for
    Source = Channel Partner
    """

    def __init__(self):
        pass

    # =====================================================
    # INTERNAL HELPERS
    # =====================================================

    def _channel_partner_df(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Returns only Channel Partner records.
        """

        if SOURCE not in df.columns:
            raise ValueError(
                f"Missing required column: {SOURCE}"
            )

        cp = df[
            df[SOURCE]
            .fillna("")
            .astype(str)
            .str.strip()
            .str.upper()
            == "CHANNEL PARTNER"
        ].copy()

        return cp

    # =====================================================
    # KPI
    # =====================================================

    def total_walkins(
        self,
        df: pd.DataFrame,
    ) -> int:

        cp = self._channel_partner_df(df)

        return len(cp)

    # -----------------------------------------------------

    def fresh_walkins(
        self,
        df: pd.DataFrame,
    ) -> int:

        cp = self._channel_partner_df(df)

        if CUSTOMER_FRESH_REVISIT not in cp.columns:
            raise ValueError(
                f"Missing required column: {CUSTOMER_FRESH_REVISIT}"
            )

        return len(

            cp[
                cp[CUSTOMER_FRESH_REVISIT]
                .fillna("")
                .astype(str)
                .str.strip()
                .str.upper()
                ==
                BUSINESS_VALUES["fresh"].upper()
            ]

        )

    # -----------------------------------------------------

    def unique_revisits(
        self,
        df: pd.DataFrame,
    ) -> int:

        cp = self._channel_partner_df(df)

        return len(

            cp[
                cp[CUSTOMER_FRESH_REVISIT]
                .fillna("")
                .astype(str)
                .str.strip()
                .str.upper()
                ==
                BUSINESS_VALUES["unique_revisit"].upper()
            ]

        )

    # -----------------------------------------------------

    def bookings(
        self,
        df: pd.DataFrame,
    ) -> int:

        cp = self._channel_partner_df(df)

        if BOOKING_DONE not in cp.columns:
            raise ValueError(
                f"Missing required column: {BOOKING_DONE}"
            )

        return len(

            cp[
                cp[BOOKING_DONE]
                .fillna("")
                .astype(str)
                .str.strip()
                .str.upper()
                == "Y"
            ]

        )

    # -----------------------------------------------------

    def conversion(
        self,
        df: pd.DataFrame,
    ) -> float:

        fresh = self.fresh_walkins(df)

        if fresh == 0:
            return 0.0

        bookings = self.bookings(df)

        return round(
            bookings / fresh * 100,
            2,
        )

    # -----------------------------------------------------

    def participating_cp(
        self,
        df: pd.DataFrame,
    ) -> int:

        cp = self._channel_partner_df(df)

        if CHANNEL_PARTNER not in cp.columns:
            raise ValueError(
                f"Missing required column: {CHANNEL_PARTNER}"
            )

        return (
            cp[CHANNEL_PARTNER]
            .dropna()
            .astype(str)
            .str.strip()
            .nunique()
        )

    # =====================================================
    # DASHBOARD
    # =====================================================

    def dashboard(
        self,
        df: pd.DataFrame,
    ) -> dict:
        """
        Returns all Reporting KPIs.

        NOTE:
        Active Channel Partners is NOT included.
        It belongs to NetworkEngine because it is
        a live KPI and not a reporting-period KPI.
        """

        total_walkins = self.total_walkins(df)
        fresh_walkins = self.fresh_walkins(df)
        unique_revisits = self.unique_revisits(df)
        bookings = self.bookings(df)
        conversion = self.conversion(df)
        participating_cp = self.participating_cp(df)

        return {

            "total_walkins": total_walkins,

            "fresh_walkins": fresh_walkins,

            "unique_revisits": unique_revisits,

            "bookings": bookings,

            "booking_count": bookings,

            "booking_percentage": conversion,

            "conversion": conversion,

            "participating_cp": participating_cp,

        }
