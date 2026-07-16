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

        self.render_highlights(
        ai,
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
    # =====================================================
    # KPI TILES
    # =====================================================

    def render_metric_tiles(
        self,
        sentiment,
        health_score,
        confidence,
    ):

        c1, c2, c3 = st.columns(3)

        with c1:

            st.markdown(
                f"""
<div class="metric-card">

<div class="metric-title">
Sentiment
</div>

<div class="metric-value">
{sentiment}
</div>

<div class="metric-footer">
Overall Business Outlook
</div>

</div>
""",
                unsafe_allow_html=True,
            )

        with c2:

            st.markdown(
                f"""
<div class="metric-card">

<div class="metric-title">
Health Score
</div>

<div class="metric-value">
{health_score}
</div>

<div class="metric-footer">
Overall Business Health
</div>

</div>
""",
                unsafe_allow_html=True,
            )

        with c3:

            st.markdown(
                f"""
<div class="metric-card">

<div class="metric-title">
AI Confidence
</div>

<div class="metric-value">
{confidence}%
</div>

<div class="metric-footer">
Evidence Confidence
</div>

</div>
""",
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)
    # =====================================================
    # PRIORITY
    # =====================================================

    def render_priority(
        self,
        priority,
    ):

        colour = "#2563eb"

        if str(priority).lower() == "high":
            colour = "#dc2626"

        elif str(priority).lower() == "medium":
            colour = "#d97706"

        elif str(priority).lower() == "low":
            colour = "#16a34a"

        st.markdown(
            f"""
<div class="priority-container">

<div class="priority-label">

Priority Status

</div>

<div
class="priority-pill"

style="background:{colour}20;color:{colour};">

{priority}

</div>

</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)
    # =====================================================
    # EXECUTIVE HIGHLIGHTS
    # =====================================================

    def render_highlights(
        self,
        ai,
    ):

        st.markdown(
            """
<div class="section-title">

Executive Intelligence Highlights

</div>
""",
            unsafe_allow_html=True,
        )

        highlights = ai.get(
            "executive_highlights",
            [],
        )

        if not highlights:

            st.markdown(
                """
<div class="highlight-empty">

No executive intelligence highlights available.

</div>
""",
                unsafe_allow_html=True,
            )

            return

        for item in highlights:

            title = item.get(
                "title",
                "",
            )

            observation = item.get(
                "observation",
                "",
            )

            evidence = item.get(
                "evidence",
                "",
            )

            st.markdown(
                f"""
<div class="highlight-card">

<div class="highlight-title">

{title}

</div>

<div class="highlight-observation">

{observation}

</div>

<div class="highlight-evidence">

{evidence}

</div>

</div>
""",
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

