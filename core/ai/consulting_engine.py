"""
=========================================================
ChannelIQ AI

Consulting Engine

Main orchestration layer for AI Consulting.

Flow

AnalysisResult
      ↓
Context Builder
      ↓
Findings Engine
      ↓
Prompt Builder
      ↓
AI Provider
      ↓
Executive Report

=========================================================
"""

from __future__ import annotations
from core.ai.executive_highlights import ExecutiveHighlights
from core.ai.executive_reasoner import ExecutiveReasoner

import json

from core.analysis_result import AnalysisResult
from core.ai.context_builder import ContextBuilder
from core.ai.findings_engine import FindingsEngine
from core.ai.provider import AIProvider
from core.ai.validator import AIResponseValidator

from core.ai.prompts import (
    SYSTEM_PROMPT,
    EXECUTIVE_REPORT_PROMPT,
    OUTPUT_FORMAT,
)


class ConsultingEngine:
    """
    Main AI Orchestrator.

    This class never talks directly to AI.

    It only talks to AIProvider.
    """

    def __init__(
        self,
        provider: AIProvider,
    ):

        self.provider = provider

        self.context_builder = ContextBuilder()

        self.findings_engine = FindingsEngine()
          
        self.executive_highlights = ExecutiveHighlights()
        self.executive_reasoner = ExecutiveReasoner()

        self.validator = AIResponseValidator()

    # =====================================================
    # PUBLIC
    # =====================================================

    def generate(
        self,
        result: AnalysisResult,
          
    ) -> dict:

        # --------------------------------------------
        # STEP 1 - Build Context
        # --------------------------------------------

        context = self.context_builder.build(result)

        print("=" * 80)
        print("STEP 1 - CONTEXT")
        print(context)
        print("=" * 80)

       
      
        # --------------------------------------------
        # STEP 2 - Executive Highlights
        # --------------------------------------------

        executive_highlights = self.executive_highlights.build(
            context
        )

        print("=" * 80)
        print("EXECUTIVE HIGHLIGHTS")
        print(executive_highlights)
        print("=" * 80)

        # --------------------------------------------
        # STEP 2 - Generate Findings
        # --------------------------------------------

        findings = self.findings_engine.analyse(context)

        executive_reasoning = self.executive_reasoner.build(
          context=context,
          executive_highlights=executive_highlights,
          findings=findings,
      )  

        print("=" * 80)
        print("STEP 2 - FINDINGS")
        print(findings)
        print("=" * 80)

        # --------------------------------------------
        # STEP 3 - Build Payload
        # --------------------------------------------

        payload = {

            "context": context,

            "executive_highlights": executive_highlights,

            "findings": findings,

            "executive_reasoning": executive_reasoning, 

        }

        # --------------------------------------------
        # STEP 4 - Build Prompt
        # --------------------------------------------

        user_prompt = self.build_prompt(payload)

        print("=" * 80)
        print("STEP 3 - PROMPT")
        print(user_prompt[:1500])
        print("=" * 80)

        # --------------------------------------------
        # STEP 5 - Call AI
        # --------------------------------------------

        response = self.provider.generate(

            system_prompt=SYSTEM_PROMPT,

            user_prompt=user_prompt,

        )

        print("=" * 80)
        print("STEP 4 - RAW AI RESPONSE")
        print(response)
        print("=" * 80)

        # --------------------------------------------
        # STEP 6 - Validate
        # --------------------------------------------

        validated = self.validator.validate(response)

        print("=" * 80)
        print("STEP 5 - VALIDATED RESPONSE")
        print(validated)
        print("=" * 80)

        return validated

    # =====================================================
    # PROMPT
    # =====================================================

    def build_prompt(
        self,
        payload: dict,
    ) -> str:

        prompt = f"""

{EXECUTIVE_REPORT_PROMPT}

========================================================

BUSINESS FACTS

========================================================

EXECUTIVE BUSINESS CONTEXT

Company

{payload["context"]["company"]}

------------------------------------------------

========================================================

EXECUTIVE CONSULTANT FACT PACK

========================================================

{json.dumps(
    payload["context"]["verified_business_facts"],
    indent=4,
    default=str
)}

------------------------------------------------

VERIFIED EXECUTIVE HIGHLIGHTS

{json.dumps(
    payload["executive_highlights"],
    indent=4,
    default=str
)}

------------------------------------------------

VERIFIED BUSINESS FINDINGS

{json.dumps(
    payload["findings"]["findings"],
    indent=4,
    default=str
)}
========================================================
AI EXECUTION INSTRUCTIONS
========================================================

The supplied information represents VERIFIED BUSINESS FACTS.

Treat every KPI, finding, executive highlight and commercial insight as fact.

Do not recalculate KPIs.

Do not invent evidence.

Use the Executive Consultant Fact Pack, Executive Highlights and Business Findings together to explain the business.

Every Executive Highlight should answer:

• What happened?
• Why does it matter?
• What commercial impact does it create?
• What specific management decision should be taken?

Use comparisons whenever possible.

Prefer named entities (Channel Partners, Sales Managers, Localities, Projects) over generic descriptions.

Recommendations must be specific, assignable and supported by evidence.

Return ONLY valid JSON.

{OUTPUT_FORMAT}
"""

        return prompt
