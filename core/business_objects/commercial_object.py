"""
=========================================================
ChannelIQ AI

Commercial Business Object

Represents Commercial Performance using
verified business facts.

=========================================================
"""

from dataclasses import dataclass, field


@dataclass
class CommercialObject:

    # -----------------------------
    # Identity
    # -----------------------------

    title: str

    category: str

    severity: str

    status: str

    # -----------------------------
    # Business Story
    # -----------------------------

    observation: str

    management_question: str

    # -----------------------------
    # Verified Evidence
    # -----------------------------

    evidence: list = field(default_factory=list)

    # -----------------------------
    # AI Layer
    # -----------------------------

    business_implication: str = ""

    management_action: str = ""
