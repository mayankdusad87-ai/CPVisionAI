"""
=========================================================
ChannelIQ AI

Excel Reader

Responsible ONLY for reading and cleaning the
standard ChannelIQ Excel template.

Responsibilities
----------------
1. Read Excel
2. Remove empty rows & columns
3. Standardize column names
4. Rename Excel headers to internal names
5. Return clean DataFrame

No business calculations should be performed here.
=========================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Union

import pandas as pd

from config import (
    EXCEL_HEADER_ROW,
    EXCEL_DATA_START_ROW,
)

from core.column_mapping import COLUMN_MAPPING


class ExcelReader:
    """
    Reads and cleans the standard ChannelIQ Excel template.
    """

    def read(
        self,
        file: Union[str, Path]
    ) -> pd.DataFrame:
        """
        Read an Excel file and return a cleaned dataframe.
        """

        df = pd.read_excel(
            file,
            header=None,
            engine="openpyxl",
        )
        print(df.iloc[:10, :5])
        return self.clean(df)

    # -----------------------------------------------------

    def clean(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Standard cleaning pipeline.
        """

        # -----------------------------------------------
        # Remove completely empty rows
        # -----------------------------------------------

        df = df.dropna(how="all")

        # -----------------------------------------------
        # Remove completely empty columns
        # -----------------------------------------------

        df = df.dropna(axis=1, how="all")

        # -----------------------------------------------
        # Actual data starts from Row 5
        # -----------------------------------------------

        df = df.iloc[
            EXCEL_DATA_START_ROW - EXCEL_HEADER_ROW:
        ]

        # -----------------------------------------------
        # Reset Index
        # -----------------------------------------------

        df.reset_index(
            drop=True,
            inplace=True,
        )

        # -----------------------------------------------
        # Clean column names
        # -----------------------------------------------

        df.columns = [

            str(col)
            .strip()
            .replace("\n", " ")

            for col in df.columns

        ]

        # -----------------------------------------------
        # Remove duplicate columns
        # -----------------------------------------------

        df = df.loc[
            :,
            ~df.columns.duplicated()
        ]

        # -----------------------------------------------
        # Rename Excel headers
        # to internal column names
        # -----------------------------------------------

                # -----------------------------------------------
        # Rename Excel headers
        # -----------------------------------------------

        df.rename(
            columns=COLUMN_MAPPING,
            inplace=True,
        )

        # -----------------------------------------------
        # Create customer_name
        # -----------------------------------------------

        if "first_name" in df.columns and "last_name" in df.columns:

            df["customer_name"] = (
                df["first_name"].fillna("").astype(str).str.strip()
                + " "
                + df["last_name"].fillna("").astype(str).str.strip()
            ).str.strip()

        return df.copy()

    # -----------------------------------------------------

    def get_columns(
        self,
        df: pd.DataFrame
    ) -> list[str]:
        """
        Return dataframe columns.
        """

        return list(df.columns)

    # -----------------------------------------------------

    def row_count(
        self,
        df: pd.DataFrame
    ) -> int:
        """
        Return total rows.
        """

        return len(df)

    # -----------------------------------------------------

    def column_count(
        self,
        df: pd.DataFrame
    ) -> int:
        """
        Return total columns.
        """

        return len(df.columns)

    # -----------------------------------------------------

    def summary(
        self,
        df: pd.DataFrame
    ) -> dict:
        """
        Returns dataframe summary.

        Useful for logging,
        debugging and upload history.
        """

        return {

            "rows": len(df),

            "columns": len(df.columns),

            "column_names": list(df.columns)

        }
