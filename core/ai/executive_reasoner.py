from __future__ import annotations


class ExecutiveReasoner:

    def build(
        self,
        context: dict,
        executive_highlights: dict,
        findings: dict,
    ) -> dict:

        return {
            "executive_story": "",
            "primary_issue": None,
            "secondary_issue": None,
            "strengths": [],
            "risks": [],
            "management_priorities": [],
            "supporting_evidence": [],
        }
