"""
=========================================================
ChannelIQ AI

Data Processor

Converts cleaned Excel data into business metrics.

Version : 1.0
=========================================================
"""


from __future__ import annotations

from datetime import datetime, timedelta

import pandas as pd

from core.kpi_engine import KPIEngine

from core.column_mapping import (
    VISIT_DATE,
    CUSTOMER_STAGE,
    CHANNEL_PARTNER,
    CLOSING_MANAGER,
    BOOKING_DATE,
    BUSINESS_VALUES,
)


class DataProcessor:
    
  def __init__(self):

    self.kpi = KPIEngine()

    """
    Extracts business metrics from the cleaned dataframe.

    This class does NOT generate AI insights.

    It only calculates facts.
    """

    def process(
        self,
        df: pd.DataFrame,
    ) -> dict:

        dashboard = self.dashboard_summary(df)

        customer = self.customer_journey(df)

        bookings = self.booking_summary(df)

        return {

            "dashboard": dashboard,

            "customer": customer,

            "bookings": bookings,

        }

    # =====================================================
    # DASHBOARD SUMMARY
    # =====================================================

    def dashboard_summary(
        self,
        df: pd.DataFrame,
    ) -> dict:

        dashboard = self.kpi.dashboard(df)

        dashboard["booking_count"] = dashboard["bookings"]

        dashboard["booking_percentage"] = dashboard["conversion"]

        fresh_walkins = self.total_fresh_walkins(df)

        return dashboard

    # =====================================================
    # CUSTOMER JOURNEY
    # =====================================================

    def customer_journey(
        self,
        df: pd.DataFrame,
    ) -> dict:

        fresh = len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["fresh"]
            ]

        )

        unique = len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["unique_revisit"]
            ]

        )

        second = len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["second_revisit"]
            ]

        )

        third = len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["third_revisit"]
            ]

        )

        fourth = len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["fourth_revisit"]
            ]

        )

        revisit = len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["revisit"]
            ]

        )

        return {

            "fresh": fresh,

            "unique_revisit": unique,

            "second_revisit": second,

            "third_revisit": third,

            "fourth_revisit": fourth,

            "revisit": revisit,

        }

    # =====================================================
    # BOOKINGS
    # =====================================================

    def booking_summary(
        self,
        df: pd.DataFrame,
    ) -> dict:

        booking_count = self.booking_count(df)

        fresh_walkins = self.total_fresh_walkins(df)

        return {

            "booking_count": booking_count,

            "booking_percentage":

                self.booking_percentage(

                    booking_count,

                    fresh_walkins,

                )

        }

    # =====================================================
    # BASIC KPI FUNCTIONS
    # =====================================================

    def total_fresh_walkins(
        self,
        df: pd.DataFrame,
    ) -> int:

        return len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["fresh"]
            ]

        )

    # -----------------------------------------------------

    def unique_revisits(
        self,
        df: pd.DataFrame,
    ) -> int:

        return len(

            df[
                df[CUSTOMER_STAGE]
                == BUSINESS_VALUES["unique_revisit"]
            ]

        )

    # -----------------------------------------------------

    def booking_count(
        self,
        df: pd.DataFrame,
    ) -> int:

        return int(

            df[BOOKING_DATE]

            .notna()

            .sum()

        )

    # -----------------------------------------------------

    def booking_percentage(
        self,
        bookings: int,
        fresh_walkins: int,
    ) -> float:

        if fresh_walkins == 0:

            return 0.0

        return round(

            (bookings / fresh_walkins) * 100,

            2,

        )

    # -----------------------------------------------------

    def active_channel_partners(
        self,
        df: pd.DataFrame,
    ) -> int:

        temp = df.copy()

        temp[VISIT_DATE] = pd.to_datetime(

            temp[VISIT_DATE],

            errors="coerce",

            dayfirst=True,

        )

        last_30_days = (

            datetime.today()

            - timedelta(days=30)

        )

        temp = temp[
            temp[VISIT_DATE]
            >= last_30_days
        ]

        return temp[
            CHANNEL_PARTNER
        ].dropna().nunique()

    # =====================================================
    # PARTNER ANALYTICS
    # =====================================================

    def partner_summary(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Returns partner level summary.

        Metrics:
        - Fresh Walk-ins
        - Total Bookings
        - Booking %
        """

        summary = (
            df.groupby(CHANNEL_PARTNER)
            .apply(self._partner_metrics)
            .reset_index()
        )

        summary = summary.sort_values(
            by="fresh_walkins",
            ascending=False
        )

        return summary

    # -----------------------------------------------------

    def top_partners_by_walkins(
        self,
        df: pd.DataFrame,
        top: int = 10,
    ) -> pd.DataFrame:

        partner_df = self.partner_summary(df)

        return partner_df.head(top)

    # -----------------------------------------------------

    def top_partners_by_bookings(
        self,
        df: pd.DataFrame,
        top: int = 10,
    ) -> pd.DataFrame:

        partner_df = self.partner_summary(df)

        return partner_df.sort_values(
            by="bookings",
            ascending=False
        ).head(top)

    # -----------------------------------------------------

    def top_partners_by_conversion(
        self,
        df: pd.DataFrame,
        top: int = 10,
    ) -> pd.DataFrame:

        partner_df = self.partner_summary(df)

        return partner_df.sort_values(
            by="booking_percentage",
            ascending=False
        ).head(top)

    # =====================================================
    # SALES MANAGER ANALYTICS
    # =====================================================

    def sales_manager_summary(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Returns Closing Manager summary.
        """

        summary = (
            df.groupby(CLOSING_MANAGER)
            .apply(self._sales_manager_metrics)
            .reset_index()
        )

        summary = summary.sort_values(
            by="fresh_walkins",
            ascending=False
        )

        return summary

    # -----------------------------------------------------

    def top_sales_managers(
        self,
        df: pd.DataFrame,
        top: int = 10,
    ) -> pd.DataFrame:

        return self.sales_manager_summary(df).head(top)

    # =====================================================
    # INTERNAL HELPERS
    # =====================================================

    def _partner_metrics(
        self,
        group: pd.DataFrame,
    ) -> pd.Series:

        fresh = len(

            group[
                group[CUSTOMER_STAGE]
                == BUSINESS_VALUES["fresh"]
            ]

        )

        bookings = int(

            group[BOOKING_DATE]
            .notna()
            .sum()

        )

        booking_percentage = 0.0

        if fresh > 0:

            booking_percentage = round(

                (bookings / fresh) * 100,

                2

            )

        return pd.Series({

            "fresh_walkins": fresh,

            "bookings": bookings,

            "booking_percentage": booking_percentage,

            "total_records": len(group)

        })

    # -----------------------------------------------------

    def _sales_manager_metrics(
        self,
        group: pd.DataFrame,
    ) -> pd.Series:

        fresh = len(

            group[
                group[CUSTOMER_STAGE]
                == BUSINESS_VALUES["fresh"]
            ]

        )

        bookings = int(

            group[BOOKING_DATE]
            .notna()
            .sum()

        )

        booking_percentage = 0.0

        if fresh > 0:

            booking_percentage = round(

                (bookings / fresh) * 100,

                2

            )

        return pd.Series({

            "fresh_walkins": fresh,

            "bookings": bookings,

            "booking_percentage": booking_percentage,

            "total_records": len(group)

        })

    # =====================================================
    # PROJECT ANALYTICS
    # =====================================================

    def project_summary(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Project-wise summary.
        """

        from core.column_mapping import PROJECT_NAME

        summary = (
            df.groupby(PROJECT_NAME)
            .size()
            .reset_index(name="walkins")
            .sort_values(
                by="walkins",
                ascending=False
            )
        )

        return summary

    # =====================================================
    # SOURCE ANALYTICS
    # =====================================================

    def source_summary(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Source-wise summary.
        """

        from core.column_mapping import SOURCE

        summary = (
            df.groupby(SOURCE)
            .size()
            .reset_index(name="walkins")
            .sort_values(
                by="walkins",
                ascending=False
            )
        )

        return summary

    # =====================================================
    # BUDGET ANALYTICS
    # =====================================================

    def budget_summary(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Budget distribution.
        """

        from core.column_mapping import BUDGET

        summary = (
            df.groupby(BUDGET)
            .size()
            .reset_index(name="customers")
            .sort_values(
                by="customers",
                ascending=False
            )
        )

        return summary

    # =====================================================
    # CONFIGURATION ANALYTICS
    # =====================================================

    def configuration_summary(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Preferred configuration distribution.
        """

        from core.column_mapping import CONFIGURATION

        summary = (
            df.groupby(CONFIGURATION)
            .size()
            .reset_index(name="customers")
            .sort_values(
                by="customers",
                ascending=False
            )
        )

        return summary

    # =====================================================
    # DORMANT PARTNERS
    # =====================================================

    def dormant_partners(
        self,
        df: pd.DataFrame,
        all_partners: list[str],
    ) -> list[str]:
        """
        Returns partners with
        zero walk-ins in the last 30 days.
        """

        temp = df.copy()

        temp[VISIT_DATE] = pd.to_datetime(
            temp[VISIT_DATE],
            errors="coerce",
            dayfirst=True,
        )

        last_30_days = datetime.today() - timedelta(days=30)

        active = temp[
            temp[VISIT_DATE] >= last_30_days
        ][CHANNEL_PARTNER].dropna().unique()

        dormant = sorted(
            list(
                set(all_partners) - set(active)
            )
        )

        return dormant

    # =====================================================
    # OVERALL DATASET SUMMARY
    # =====================================================

    def dataset_summary(
        self,
        df: pd.DataFrame,
    ) -> dict:
        """
        General dataset statistics.
        """

        return {

            "rows": len(df),

            "columns": len(df.columns),

            "unique_customers":
                df["mobile"].nunique(),

            "unique_projects":
                df["project_name"].nunique(),

            "unique_partners":
                df["channel_partner"].nunique(),

            "unique_sales_managers":
                df["closing_manager"].nunique(),

        }
