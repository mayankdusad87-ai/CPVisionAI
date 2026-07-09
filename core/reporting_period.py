"""
=========================================================
ChannelIQ AI

Reporting Period Engine

Responsible for:

1. Discovering available reporting periods
2. Returning latest reporting period
3. Filtering dataframe by reporting period

=========================================================
"""

from __future__ import annotations

import pandas as pd


class ReportingPeriod:

    """
    Reporting Period Engine

    This module is the single source of truth
    for all month/year filtering.
    """

    # ----------------------------------------------------

    def prepare_dates(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        """
        Converts visit_date into datetime.
        """

        df = df.copy()

        df["visit_date"] = pd.to_datetime(

            df["visit_date"],

            dayfirst=True,

            errors="coerce",

        )

        return df

    # ----------------------------------------------------

    def available_periods(
        self,
        df: pd.DataFrame,
    ) -> list[str]:

        """
        Returns all available months
        sorted chronologically.
        """

        df = self.prepare_dates(df)

        periods = (

            df["visit_date"]

            .dropna()

            .dt.to_period("M")

            .unique()

        )

        periods = sorted(periods)

        return [

            p.strftime("%B %Y")

            for p in periods

        ]

    # ----------------------------------------------------

    def latest_period(
        self,
        df: pd.DataFrame,
    ) -> str | None:

        """
        Returns latest available month.
        """

        periods = self.available_periods(df)

        if not periods:

            return None

        return periods[-1]

    # ----------------------------------------------------

    def filter(
        self,
        df: pd.DataFrame,
        period: str,
    ) -> pd.DataFrame:

        """
        Returns dataframe filtered
        for selected month.
        """

        df = self.prepare_dates(df)

        period_date = pd.to_datetime(

            period,

            format="%B %Y",

        )

        filtered = df[

            (df["visit_date"].dt.month == period_date.month)

            &

            (df["visit_date"].dt.year == period_date.year)

        ]

        return filtered.reset_index(drop=True)

    # ----------------------------------------------------

    def summary(
        self,
        df: pd.DataFrame,
    ) -> dict:

        """
        Dashboard helper.
        """

        return {

            "available_periods": self.available_periods(df),

            "latest_period": self.latest_period(df),

            "record_count": len(df),

        }
