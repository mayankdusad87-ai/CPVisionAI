"""
=========================================================
ChannelIQ AI

KPI Engine

Single source of truth for all KPI calculations.

All KPIs are calculated ONLY for

Source = Channel Partner

=========================================================
"""

from __future__ import annotations

import pandas as pd


class KPIEngine:

    def __init__(self):

        pass

    # --------------------------------------------------

    def _channel_partner_df(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Returns only Channel Partner records.
        """

        return df[
            df["source"]
            .fillna("")
            .astype(str)
            .str.strip()
            .str.upper()
            == "CHANNEL PARTNER"
        ].copy()

    # --------------------------------------------------

    def total_walkins(
        self,
        df: pd.DataFrame,
    ) -> int:
        """
        Total Walk-ins

        Source = Channel Partner
        """

        cp = self._channel_partner_df(df)

        return len(cp)

    # --------------------------------------------------

    def fresh_walkins(
        self,
        df: pd.DataFrame,
    ) -> int:
        """
        Fresh Walk-ins

        Source = Channel Partner

        AND

        Customer Fresh/Revisit = Fresh
        """

        cp = self._channel_partner_df(df)

        return len(

            cp[
                cp["customer_fresh_revisit"]
                .fillna("")
                .astype(str)
                .str.strip()
                .str.upper()
                == "FRESH"
            ]

        )

    # --------------------------------------------------

    def unique_revisits(
        self,
        df: pd.DataFrame,
    ) -> int:
        """
        Unique Revisits
        """

        cp = self._channel_partner_df(df)

        return len(

            cp[
                cp["customer_fresh_revisit"]
                .fillna("")
                .astype(str)
                .str.strip()
                .str.upper()
                == "UNIQUE REVISIT"
            ]

        )

    # --------------------------------------------------

    def bookings(
        self,
        df: pd.DataFrame,
    ) -> int:
        """
        Bookings

        Booking Done = Y

        Source = Channel Partner
        """

        cp = self._channel_partner_df(df)

        return len(

            cp[
                cp["booking_done"]
                .fillna("")
                .astype(str)
                .str.strip()
                .str.upper()
                == "Y"
            ]

        )

    # --------------------------------------------------

    def conversion(
        self,
        df: pd.DataFrame,
    ) -> float:

        fresh = self.fresh_walkins(df)

        bookings = self.bookings(df)

        if fresh == 0:

            return 0

        return round(

            bookings / fresh * 100,

            2,

        )

    # --------------------------------------------------

    def active_channel_partners(
        self,
        df: pd.DataFrame,
    ) -> int:
        """
        Unique Active Channel Partners
        """

        cp = self._channel_partner_df(df)

        return (

            cp["channel_partner"]

            .dropna()

            .astype(str)

            .str.strip()

            .nunique()

        )

    # --------------------------------------------------

    def dashboard(
        self,
        df: pd.DataFrame,
    ) -> dict:
        """
        Returns all dashboard KPIs.
        """

        return {

            "total_walkins": self.total_walkins(df),

            "fresh_walkins": self.fresh_walkins(df),

            "unique_revisits": self.unique_revisits(df),

            "bookings": self.bookings(df),

            "conversion": self.conversion(df),

            "active_channel_partners": self.active_channel_partners(df),

        }
