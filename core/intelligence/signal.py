"""
=========================================================
ChannelIQ AI

Business Intelligence Signal

Base model used by every intelligence engine.

=========================================================
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class Signal:

    # Identity
    id: str
    title: str
    category: str

    # Classification
    severity: str
    status: str

    # Business narrative
    summary: str
    business_impact: str
    management_question: str

    # Supporting data
    evidence: Dict[str, Any] = field(default_factory=dict)

    # Recommended actions
    recommendations: List[str] = field(default_factory=list)

    # Extra information
    metadata: Dict[str, Any] = field(default_factory=dict)
