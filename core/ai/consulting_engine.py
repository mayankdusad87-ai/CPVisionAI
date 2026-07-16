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

BUSINESS SNAPSHOT

{payload["context"]["business_snapshot"]}

------------------------------------------------

COMMERCIAL INTELLIGENCE

{payload["context"].get("commercial_intelligence", {})}

------------------------------------------------

EXECUTIVE HIGHLIGHTS (VERIFIED)

{json.dumps(payload["executive_highlights"], indent=4, default=str)}

------------------------------------------------

KEY VERIFIED FINDINGS

{json.dumps(payload["findings"]["findings"], indent=4, default=str)}

------------------------------------------------

BUSINESS FACTS (FULL)

{json.dumps(payload, indent=4, default=str)}

========================================================

IMPORTANT

========================================================
The Executive Highlights are VERIFIED BUSINESS OBSERVATIONS.

Do NOT create new executive highlights.

For each Executive Highlight:

1. Explain why it matters.
2. Explain the business implication.
3. Recommend a management action.

Do not change the observation.

Do not change the evidence.

Observation and Evidence are already verified by the Business Engine.

Use ONLY supplied business facts.

Never invent KPIs.

Never invent numbers.

Never contradict supplied metrics.

{OUTPUT_FORMAT}

"""

        return prompt
