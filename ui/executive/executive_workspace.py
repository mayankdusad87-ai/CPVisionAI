"""
=========================================================
ChannelIQ AI

Executive Workspace

Enterprise Executive Report UI

=========================================================
"""

from __future__ import annotations

import streamlit as st


class ExecutiveWorkspace:

    # =====================================================
    # PUBLIC
    # =====================================================

    def render(
        self,
        result,
        ai,
    ):

        health = ai.get(
            "health_snapshot",
            {},
        )

        reporting_period = result.metadata.get(
            "reporting_period",
            "-",
        )

        analysis_id = result.analysis_id

        sentiment = health.get(
            "status",
            "-",
        )

        health_score = health.get(
            "score",
            "-",
        )

        confidence = health.get(
            "confidence",
            0,
        )

        priority = health.get(
            "management_priority",
            "Normal",
        )

        st.markdown(
            """
<div class="executive-page">
""",
            unsafe_allow_html=True,
        )

        self.render_header()

        self.render_brief_header(
            reporting_period,
            analysis_id,
        )

        self.render_metric_tiles(
            sentiment,
            health_score,
            confidence,
        )

        self.render_priority(
            priority,
        )
    # =====================================================
    # HEADER
    # =====================================================

    def render_header(self):

        st.markdown(
            """
<div class="executive-report-header">

    <div>

        <div class="executive-report-title">

            📊 Executive Intelligence Report

        </div>

        <div class="executive-report-subtitle">

            AI Powered Business Intelligence

        </div>

    </div>

</div>
""",
            unsafe_allow_html=True,
        )
            # =====================================================
    # EXECUTIVE BRIEF
    # =====================================================

    def render_brief_header(
        self,
        reporting_period,
        analysis_id,
    ):

        left, right = st.columns(
            [3, 1],
        )

        with left:

            st.markdown(
                """
<div class="executive-card">

<div class="executive-card-title">

Executive Intelligence Brief

</div>

<div class="executive-card-subtitle">

OFFICIAL EXECUTIVE INTELLIGENCE BRIEFING

</div>

</div>
""",
                unsafe_allow_html=True,
            )

        with right:

            st.markdown(
                f"""
<div class="metadata-card">

<div class="meta-heading">

Reporting Period

</div>

<div class="meta-value">

{reporting_period}

</div>

<br>

<div class="meta-heading">

Analysis ID

</div>

<div class="meta-value">

{analysis_id}

</div>

</div>
""",
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

