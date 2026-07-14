"""
=========================================================
ChannelIQ AI

AI Response Validator

Validates and normalizes the AI response.

Responsibilities
----------------
1. Validate required keys
2. Add missing sections
3. Prevent app crashes
4. Normalize response structure

=========================================================
"""

from __future__ import annotations

from typing import Any


class AIResponseValidator:
    """
    Validates AI responses and ensures a
    consistent structure for the UI.
    """

    DEFAULT_RESPONSE = {

        "health_snapshot": {
    
            "status": "",
    
            "score": 0,
    
            "confidence": 0,
    
            "management_priority": ""
    
        },
    
        "business_brief": "",
    
        "executive_summary": "",
    
        "diagnosis": "",
    
        "key_findings": [],
    
        "root_causes": [],
    
        "risks": [],
    
        "opportunities": [],
    
        "recommendations": [],
    
        "monday_plan": [],
    
        "leadership_questions": [],
    
    }
    # =====================================================
    # PUBLIC
    # =====================================================

    def validate(
        self,
        response: dict[str, Any] | None,
    ) -> dict[str, Any]:

        """
        Ensures all required keys exist.

        Returns a normalized dictionary.
        """

        if response is None:

            return self.DEFAULT_RESPONSE.copy()

        if not isinstance(response, dict):

            return self.DEFAULT_RESPONSE.copy()

        validated = self.DEFAULT_RESPONSE.copy()

        for key in validated:

            if key in response:

                validated[key] = response[key]

        return validated

    # =====================================================
    # STATUS
    # =====================================================

    def is_valid(
        self,
        response: dict[str, Any] | None,
    ) -> bool:

        if response is None:

            return False

        if not isinstance(response, dict):

            return False

        required = [

            "health_snapshot",
            "business_brief",

            "executive_summary",
        
            "diagnosis",
        
            "key_findings",
        
            "root_causes",
        
            "risks",
        
            "opportunities",
        
            "recommendations",
        
            "monday_plan",
        
            "leadership_questions",



        ]

        return all(

            key in response

            for key in required

        )
