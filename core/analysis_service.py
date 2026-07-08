"""
=========================================================
ChannelIQ AI

Analysis Service

Main orchestration layer.

Flow

Excel
    ↓
ExcelReader
    ↓
TemplateValidator
    ↓
DataProcessor
    ↓
PartnerAnalyzer
    ↓
AnalysisResult

=========================================================
"""

from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from core.analysis_result import AnalysisResult
from core.excel_reader import ExcelReader
from core.data_processor import DataProcessor
from core.partner_analyzer import PartnerAnalyzer

from utils.validators import TemplateValidator


class AnalysisService:

    """
    Main orchestration class.

    Every uploaded Excel passes through this class.
    """

    def __init__(self):

        self.reader = ExcelReader()

        self.validator = TemplateValidator()

        self.processor = DataProcessor()

        self.partner_analyzer = PartnerAnalyzer()

    # =====================================================
    # PUBLIC
    # =====================================================

    def analyse(

        self,

        excel_file,

        company_name: str,

        project_name: str,

        month: str,

        year: int,

    ) -> AnalysisResult:

        result = AnalysisResult()

        # -----------------------------------------
        # Metadata
        # -----------------------------------------

        result.analysis_id = (

            datetime.now().strftime("%Y%m%d")

            + "-"

            + uuid4().hex[:8].upper()

        )

        result.company_name = company_name

        result.project_name = project_name

        result.month = month

        result.year = year

        # -----------------------------------------
        # Read Excel
        # -----------------------------------------

        df = self.reader.read(excel_file)
        
        print(df.columns.tolist())
        # -----------------------------------------
        # Validate
        # -----------------------------------------

        self.validator.run(df)

        result.dataframe = df

        # -----------------------------------------
        # Process Business Metrics
        # -----------------------------------------

        processed = self.processor.process(df)

        dashboard = processed["dashboard"]

        customer = processed["customer"]

        bookings = processed["bookings"]

        # -----------------------------------------
        # Partner Analytics
        # -----------------------------------------

        partner_df = self.processor.partner_summary(df)

        partner_analysis = self.partner_analyzer.report(

            partner_df

        )

        # -----------------------------------------
        # Populate AnalysisResult
        # -----------------------------------------

        result.total_bookings = dashboard["booking_count"]

        result.conversion = dashboard["booking_percentage"]

        result.metadata = {

            "fresh_walkins":

                dashboard["fresh_walkins"],

            "unique_revisits":

                dashboard["unique_revisits"],

            "active_channel_partners":

                dashboard["active_channel_partners"],

            "customer_journey":

                customer,

            "booking_summary":

                bookings,

            "partner_summary":

                partner_analysis,

            "generated_at":

                datetime.now(),

        }

        # -----------------------------------------
        # Executive Summary
        # -----------------------------------------

        result.executive_summary = (

            partner_analysis["executive_summary"]

        )

        result.recommendations = (

            partner_analysis["recommendations"]

        )

        return result
