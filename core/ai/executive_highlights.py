"""
=========================================================
ChannelIQ AI

Executive Intelligence Highlights

Creates the Executive Intelligence section
shown at the top of the report.

=========================================================
"""

from __future__ import annotations

from typing import Any


class ExecutiveHighlights:

    def build(
        self,
        context: dict[str, Any],
    ) -> list[dict]:

        highlights = []

        commercial = context.get(
            "commercial_intelligence",
            None,
        )

        if commercial:

            highlights.append(

                {

                    "title": commercial.title,

                    "observation": commercial.summary,

                    "evidence": commercial.evidence,

                }

            )

        return highlights
