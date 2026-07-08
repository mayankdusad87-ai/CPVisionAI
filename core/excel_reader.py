"""
=========================================================
ChannelIQ AI

Excel Reader

Responsible ONLY for reading the standard
ChannelIQ Excel template.

Business calculations are NOT performed here.
=========================================================
"""

from __future__ import annotations
from core.column_mapping import COLUMN_MAPPING

from pathlib import Path
from typing import Union

import pandas as pd

from config import (
    EXCEL_HEADER_ROW,
    EXCEL_DATA_START_ROW,
)


class ExcelReader:
    """
    Reads the ChannelIQ Excel template.

    Template Standard

    Header Row : 4
    Data Row   : 5 onwards
    """

    def read(
        self,
        file: Union[str, Path]
    ) -> pd.DataFrame:

        # -----------------------------
        # Read Excel
        # -----------------------------

        df = pd.read_excel(
            file,
            header=EXCEL_HEADER_ROW - 1,
            engine="openpyxl",
        )

        return self.clean(df)

    # ----------------------------------------------------

    def clean(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        """
        Standard cleaning applied
        to every uploaded template.
        """

        # Remove empty rows

        df = df.dropna(how="all")

        # Data begins from Row 5

        df = df.iloc[
            EXCEL_DATA_START_ROW - EXCEL_HEADER_ROW:
        ]

        # Reset index

        df.reset_index(
            drop=True,
            inplace=True,
        )

        # Clean column names

        df.columns = [

            str(col).strip()

            for col in df.columns

        ]
        df.rename(
            columns=COLUMN_MAPPING,
            inplace=True,
        )

        # Remove duplicate columns

        df = df.loc[
            :,
            ~df.columns.duplicated()
        ]

        return df

    # ----------------------------------------------------

    def get_columns(
        self,
        df: pd.DataFrame
    ) -> list[str]:

        return list(df.columns)

    # ----------------------------------------------------

    def row_count(
        self,
        df: pd.DataFrame
    ) -> int:

        return len(df)

    # ----------------------------------------------------

    def column_count(
        self,
        df: pd.DataFrame
    ) -> int:

        return len(df.columns)
