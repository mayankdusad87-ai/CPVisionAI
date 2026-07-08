"""
=========================================================
ChannelIQ AI

Analysis Service

Coordinates the complete business analysis workflow.

Flow

Excel
    ↓
Excel Reader
    ↓
Validation
    ↓
Data Processor
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
from utils.validators import TemplateValidator


class AnalysisService:
    """
    Main orchestration layer.

    This class does not contain business calculations.
    It coordinates the complete analysis pipeline.
    """

    def __init__(self):

        self.reader = ExcelReader()

        self.validator = TemplateValidator()

        self.processor = DataProcessor()

    # ======================================================

    def analyse(
        self,
        excel_file,
        company_name: str,
        project_name: str,
        month: str,
        year: int,
    ) -> AnalysisResult:

        # ---------------------------------------------
        # Create a fresh AnalysisResult
        # ---------------------------------------------

        result = AnalysisResult()

        self._initialise_metadata(

            result,

            company_name,

            project_name,

            month,

            year,

        )

        # ---------------------------------------------
        # Read Excel
        # ---------------------------------------------

        df = self.reader.read(excel_file)

        # ---------------------------------------------
        # Validate template
        # ---------------------------------------------

        self.validator.validate(df)

        result.dataframe = df

        # ---------------------------------------------
        # Process business metrics
        # ---------------------------------------------

        metrics = self.processor.process(df)

        # ---------------------------------------------
        # Populate AnalysisResult
        # ---------------------------------------------

        result.total_bookings = metrics["booking_count"]

        result.conversion = metrics["booking_percentage"]

        result.metadata = {

            "rows": metrics["total_records"],

            "columns": len(df.columns),

            "fresh_walkins": metrics["fresh_walkins"],

            "unique_revisits": metrics["unique_revisits"],

            "active_channel_partners":
                metrics["active_channel_partners"],

            "generated_at":
                datetime.now().isoformat(),

        }

        # Temporary placeholders
        # These will be replaced by later engines

        result.health_score = 0

        result.revenue_opportunity = 0

        result.growth_rate = 0

        result.high_risk_partners = 0

        return result

    # ======================================================

    def _initialise_metadata(

        self,

        result: AnalysisResult,

        company: str,

        project: str,

        month: str,

        year: int,

    ):

        result.analysis_id = (

            datetime.now().strftime("%Y%m%d")

            + "-"

            + uuid4().hex[:8].upper()

        )

        result.company_name = company

        result.project_name = project

        result.month = month

        result.year = year
