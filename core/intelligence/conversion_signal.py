"""
=========================================================
ChannelIQ AI

Commercial Conversion Signal

Sprint 5.1.1

=========================================================
"""

from __future__ import annotations

from config import AVERAGE_BOOKING_VALUE
from core.intelligence.signal import Signal


class ConversionSignal:
    """
    Commercial Conversion Intelligence

    Business Dictionary

    Overall Fresh Walk-ins
        Customer Fresh/Revisit = Fresh

    Overall Bookings
        Booking Done = Y

    CP Fresh Walk-ins
        Source = Channel Partner
        AND Fresh

    CP Bookings
        Source = Channel Partner
        AND Booking Done = Y
    """

    def analyse(self, df):

        # ==================================================
        # Overall Fresh Walk-ins
        # ==================================================

        overall_fresh_walkins = len(

            df[
                df["customer_fresh_revisit"]
                .astype(str)
                .str.strip()
                .str.upper()
                == "FRESH"
            ]

        )

        # ==================================================
        # Overall Bookings
        # ==================================================

        overall_bookings = len(

            df[
                df["booking_done"]
                .astype(str)
                .str.strip()
                .str.upper()
                == "Y"
            ]

        )

        # ==================================================
        # CP Fresh Walk-ins
        # ==================================================

        cp_fresh_walkins = len(

            df[

                (df["source"]
                    .astype(str)
                    .str.strip()
                    .str.upper()
                    == "CHANNEL PARTNER")

                &

                (df["customer_fresh_revisit"]
                    .astype(str)
                    .str.strip()
                    .str.upper()
                    == "FRESH")

            ]

        )

        # ==================================================
        # CP Bookings
        # ==================================================

        cp_bookings = len(

            df[

                (df["source"]
                    .astype(str)
                    .str.strip()
                    .str.upper()
                    == "CHANNEL PARTNER")

                &

                (df["booking_done"]
                    .astype(str)
                    .str.strip()
                    .str.upper()
                    == "Y")

            ]

        )

        # ==================================================
        # Conversion
        # ==================================================

        overall_conversion = (

            overall_bookings / overall_fresh_walkins * 100

            if overall_fresh_walkins

            else 0

        )

        cp_conversion = (

            cp_bookings / cp_fresh_walkins * 100

            if cp_fresh_walkins

            else 0

        )

        conversion_gap = (

            cp_conversion - overall_conversion

        )

        # ==================================================
        # Expected Bookings
        # ==================================================

        expected_cp_bookings = (

            cp_fresh_walkins

            * overall_conversion

            / 100

        )

        lost_bookings = max(

            0,

            round(expected_cp_bookings - cp_bookings)

        )

        revenue_opportunity = (

            lost_bookings

            * AVERAGE_BOOKING_VALUE

        )

        # ==================================================
        # Severity
        # ==================================================

        if overall_bookings == 0:

            severity = "Critical"

            status = "Negative"

            summary = (

                "No bookings were recorded during the reporting period."

            )

        else:

            if conversion_gap >= 0:

                severity = "Excellent"

                status = "Positive"

                summary = (

                    "Channel Partner conversion is meeting or exceeding the overall project conversion."

                )

            elif conversion_gap >= -1:

                severity = "Low"

                status = "Neutral"

                summary = (

                    "Channel Partner conversion is marginally below the project average."

                )

            elif conversion_gap >= -3:

                severity = "Medium"

                status = "Negative"

                summary = (

                    "Channel Partner conversion is below the project benchmark and requires management attention."

                )

            else:

                severity = "Critical"

                status = "Negative"

                summary = (

                    "Channel Partner conversion is significantly below the project benchmark."

                )

        # ==================================================
        # Signal
        # ==================================================

        signal = Signal(

            id="commercial_conversion",

            title="Commercial Conversion",

            category="Commercial",

            severity=severity,

            status=status,

            summary=summary,

            business_impact=(

                f"Estimated opportunity of "

                f"{lost_bookings} additional bookings "

                f"worth approximately ₹{revenue_opportunity:,.0f}."

            ),

            management_question=(

                "Is the Channel Partner network helping or hurting overall project conversion?"

            ),

            evidence={

                "overall_fresh_walkins": overall_fresh_walkins,

                "overall_bookings": overall_bookings,

                "overall_conversion": round(overall_conversion, 2),

                "cp_fresh_walkins": cp_fresh_walkins,

                "cp_bookings": cp_bookings,

                "cp_conversion": round(cp_conversion, 2),

                "conversion_gap": round(conversion_gap, 2),

                "expected_cp_bookings": round(expected_cp_bookings),

                "lost_bookings": lost_bookings,

                "revenue_opportunity": revenue_opportunity,

            },

        )

        return signal
