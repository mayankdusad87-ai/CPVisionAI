"""
=========================================================
ChannelIQ AI

Executive Reasoner

Transforms verified business evidence into
executive reasoning.

Responsibilities

Verified Facts
        ↓
Normalize
        ↓
Prioritize
        ↓
Narrative

=========================================================
"""

from __future__ import annotations


class ExecutiveReasoner:

    def build(
        self,
        context: dict,
        executive_highlights: dict,
        findings: dict,
    ) -> dict:

        evidence = self._collect_evidence(
            context,
            executive_highlights,
            findings,
        )

        normalized = self._normalize_evidence(
            evidence,
        )

        reasoning = self._build_reasoning(
            normalized,
        )

        return reasoning
      def _collect_evidence(
    self,
    context,
    executive_highlights,
    findings,
):

    return {

        "facts": context.get(
            "verified_business_facts",
            {}
        ),

        "highlights": executive_highlights,

        "findings": findings,
    }
