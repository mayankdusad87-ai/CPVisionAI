"""
=========================================================
ChannelIQ AI

Validation Utilities

Validates the cleaned dataframe returned by
ExcelReader.

Version : 2.0
=========================================================
"""

from __future__ import annotations

import pandas as pd

from core.column_mapping import (
    FORM_NO,
    VISIT_DATE,
    CUSTOMER_NAME,
    MOBILE,
    CUSTOMER_FRESH_REVISIT,
    CHANNEL_PARTNER,
    CLOSING_MANAGER,
)


class TemplateValidationError(Exception):
    """
    Raised when the uploaded template
    is missing required columns.
    """
    pass


class TemplateValidator:

    def __init__(self):

        self.required_columns = [

            FORM_NO,

            VISIT_DATE,

            CUSTOMER_NAME,

            MOBILE,

            CUSTOMER_FRESH_REVISIT,

            CHANNEL_PARTNER,

            CLOSING_MANAGER,

        ]

    # ----------------------------------------------------

    def validate(
        self,
        df: pd.DataFrame,
    ) -> None:
        """
        Validate cleaned dataframe.
        """

        if df.empty:

            raise TemplateValidationError(

                "The uploaded Excel file contains no data."

            )

        missing = [

            column

            for column in self.required_columns

            if column not in df.columns

        ]

        if missing:

            raise TemplateValidationError(

                "Missing required columns:\n\n"

                + "\n".join(missing)

            )

    # ----------------------------------------------------

    def validate_not_empty(
        self,
        df: pd.DataFrame,
    ) -> None:

        if len(df) == 0:

            raise TemplateValidationError(

                "The uploaded file has zero records."

            )

    # ----------------------------------------------------

    def validate_duplicates(
        self,
        df: pd.DataFrame,
    ) -> None:
        """
        Placeholder for future duplicate checks.
        """

        return

    # ----------------------------------------------------

    def validate_business_rules(
        self,
        df: pd.DataFrame,
    ) -> None:
        """
        Placeholder for future business validations.
        """

        return

    # ----------------------------------------------------

    def run(
        self,
        df: pd.DataFrame,
    ) -> None:
        """
        Execute all validations.
        """

        self.validate(df)

        self.validate_not_empty(df)

        self.validate_duplicates(df)

        self.validate_business_rules(df)
