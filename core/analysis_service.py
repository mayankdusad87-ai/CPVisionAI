"""
=========================================================
ChannelIQ AI

Analysis Service

=========================================================
"""

from __future__ import annotations

import traceback

from datetime import datetime
from uuid import uuid4

from core.analysis_result import AnalysisResult
from core.data_processor import DataProcessor
from core.excel_reader import ExcelReader
from core.partner_analyzer import PartnerAnalyzer
from core.partner_engine import PartnerEngine
from core.reporting_period import ReportingPeriod

from core.ai.consulting_engine import ConsultingEngine
from core.ai.groq_provider import GroqProvider

from utils.validators import TemplateValidator


class AnalysisService:

    def __init__(self):

        self.reader = ExcelReader()

        self.validator = TemplateValidator()

        self.processor = DataProcessor()

        self.partner_engine = PartnerEngine()

        self.partner_analyzer = PartnerAnalyzer()

        self.reporting = ReportingPeriod()

        self.ai_provider = GroqProvider()
        print("=" * 80)
        print("OPENAI HEALTH:", self.ai_provider.health_check())
        print("=" * 80)

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

        # ----------------------------------------------

        result.analysis_id = (

            datetime.now().strftime("%Y%m%d")

            + "-"

            + uuid4().hex[:8].upper()

        )

        result.company_name = company_name

        result.project_name = project_name

        result.month = reporting_period or ""

        result.year = 0

        # ----------------------------------------------

        full_df = dataframe.copy()

        self.validator.run(full_df)

        # ----------------------------------------------

        available_periods = (

            self.reporting.available_periods(full_df)

        )

        latest_period = (

            self.reporting.latest_period(full_df)

        )

        if reporting_period is None:

            reporting_period = latest_period

        df = self.reporting.filter(

            full_df,

            reporting_period,

        )

        result.dataframe = df

        # ----------------------------------------------
        # KPI ENGINE
        # ----------------------------------------------
        print("STEP 1")
        processed = self.processor.process(df)

        dashboard = processed["dashboard"]

        customer = processed["customer"]

        bookings = processed["bookings"]
        print("STEP 2")

        if not isinstance(dashboard, dict):

            raise ValueError(

                "Dashboard was not returned."

            )

        # ----------------------------------------------
        # PARTNER ENGINE
        # ----------------------------------------------
        print("STEP 3")
        partner_df = self.partner_engine.analyse(df)
        print("STEP 4")
        print(partner_df.head())

        partner_analysis = (

            self.partner_analyzer.report(

                partner_df

            )

        )
        # ----------------------------------------------
        # Populate Result
        # ----------------------------------------------

        result.total_bookings = dashboard.get("bookings", 0)

        result.conversion = dashboard.get("conversion", 0)

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
        # ----------------------------------------------
        # TEST - COMMERCIAL CONVERSION SIGNAL
        # ----------------------------------------------


                
        from core.intelligence.conversion_signal import ConversionSignal
        
        signal = ConversionSignal().analyse(df)

        result.metadata["commercial_intelligence"] = {

        "title": signal.title,
    
        "category": signal.category,
    
        "severity": signal.severity,
    
        "status": signal.status,
    
        "summary": signal.summary,
    
        "business_impact": signal.business_impact,
    
        "management_question": signal.management_question,
    
        "evidence": signal.evidence,    

  }
        
        


        

        # ----------------------------------------------
        # AI Consulting
        # ----------------------------------------------

        try:

            result.ai_report = self.consulting.generate(result)
        

        except Exception as ex:

            print("=" * 80)

            print("AI CONSULTING ERROR")

            print(ex)

            print("=" * 80)

            result.ai_report = {}

        # ----------------------------------------------
        # Executive Summary
        # ----------------------------------------------

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


