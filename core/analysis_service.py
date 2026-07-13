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
ReportingPeriod
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

from core.partner_engine import PartnerEngine
from core.reporting_period import ReportingPeriod
from core.ai.consulting_engine import ConsultingEngine
from core.ai.openai_provider import OpenAIProvider

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

        self.reporting = ReportingPeriod()

        self.ai_provider = OpenAIProvider()

        self.consulting = ConsultingEngine(
           self.ai_provider
        )
    # =====================================================
    # PUBLIC
    # =====================================================

    def analyse(
        self,
        dataframe,
        company_name: str,
        project_name: str,
        reporting_period: str | None = None,
    ) -> AnalysisResult:

        result = AnalysisResult()

        # -------------------------------------------------
        # Metadata
        # -------------------------------------------------

        result.analysis_id = (
            datetime.now().strftime("%Y%m%d")
            + "-"
            + uuid4().hex[:8].upper()
        )

        result.company_name = company_name
        result.project_name = project_name

        result.month = reporting_period or ""
        result.year = 0

        # -------------------------------------------------
        # Read Excel
        # -------------------------------------------------

        full_df = dataframe.copy()

        # -------------------------------------------------
        # Validate
        # -------------------------------------------------

        self.validator.run(full_df)

        # -------------------------------------------------
        # Reporting Period
        # -------------------------------------------------

        available_periods = self.reporting.available_periods(full_df)

        latest_period = self.reporting.latest_period(full_df)

        if reporting_period is None:

            reporting_period = latest_period

        df = self.reporting.filter(
            full_df,
            reporting_period,
        )

      

       

        # -------------------------------------------------
        # Process Business Metrics
        # -------------------------------------------------

        processed = self.processor.process(df)

        dashboard = processed["dashboard"]

        if not isinstance(dashboard, dict):
           raise ValueError(
               "KPI Engine did not return a dashboard dictionary." 
           )

        customer = processed["customer"]

        bookings = processed["bookings"]

        # -------------------------------------------------
        # Partner Analytics
        # -------------------------------------------------

        partner_df = PartnerEngine().analyse(df)
        partner_df = partner_engine.analyse(df)

        partner_analysis = self.partner_analyzer.report(
          partner_df
        )

        # -------------------------------------------------
        # Populate Analysis Result
        # -------------------------------------------------

        result.total_bookings = dashboard["bookings"]

        result.conversion = dashboard["conversion"]

        result.metadata = {

            "available_periods": available_periods,

            "reporting_period": reporting_period,

            "total_walkins": dashboard.get("total_walkins", 0),

            "fresh_walkins": dashboard.get("fresh_walkins", 0),

            "unique_revisits": dashboard.get("unique_revisits", 0),

            "participating_cp": dashboard.get("participating_cp", 0),

            "customer_journey": customer,

            "booking_summary": bookings,

            "partner_summary": partner_analysis,
 
            "partner_table": partner_df,

            "generated_at": datetime.now(),

        }
        # -------------------------------------------------
        # AI Consulting
        # -------------------------------------------------
        
        try:
        
            result.ai_report = self.consulting.generate(result)
        
            print("=" * 80)
            print("AI REPORT")
            print(result.ai_report)
            print("=" * 80)
        
        except Exception as ex:
        
            print("=" * 80)
            print("AI CONSULTING ERROR")
            print(ex)
            print("=" * 80)
        
            result.ai_report = {}
        # -------------------------------------------------
        # Executive Summary
        # -------------------------------------------------

       if result.ai_report:

        result.executive_summary = result.ai_report.get(
            "executive_summary",
            "",
        )
    
        result.recommendations = result.ai_report.get(
            "recommendations",
            [],
        )

    else:
    
        result.executive_summary = (
            partner_analysis["executive_summary"]
        )
    
        result.recommendations = (
            partner_analysis["recommendations"]
        )
    
    return result
