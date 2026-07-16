"""
=========================================================
ChannelIQ

Executive Workspace

=========================================================
"""

import streamlit as st
from html import escape


class ExecutiveWorkspace:

    def render(self, result, ai):

        html = self._build_page(result, ai)

        st.markdown(
            html,
            unsafe_allow_html=True,
        )

    def _build_page(
        self,
        result,
        ai,
):

    health = ai.get("health_snapshot", {})

    status = health.get("status", "-")
    score = health.get("score", "-")
    confidence = health.get("confidence", 0)
    priority = health.get("management_priority", "Not Available")

    reporting_period = result.metadata.get(
        "reporting_period",
        "-",
    )

    analysis_id = result.analysis_id

    html = f"""

<div class="executive-wrapper">

    <div class="executive-card">

        <div class="executive-top">

            <div>

                <div class="executive-title">

                    📊 Executive Intelligence Report

                </div>

                <div class="executive-subtitle">

                    Executive Intelligence Brief

                </div>

            </div>

            <div class="metadata-card">

                <div class="meta-label">

                    Reporting Period

                </div>

                <div class="meta-value">

                    {escape(str(reporting_period))}

                </div>

                <div class="meta-label">

                    Analysis ID

                </div>

                <div class="meta-value">

                    {escape(str(analysis_id))}

                </div>

            </div>

        </div>

        <div class="metric-grid">

            <div class="metric-box">

                <div class="metric-label">

                    SENTIMENT

                </div>

                <div class="metric-number">

                    {escape(str(status))}

                </div>

                <div class="metric-description">

                    Overall Business Outlook

                </div>

            </div>

            <div class="metric-box">

                <div class="metric-label">

                    HEALTH SCORE

                </div>

                <div class="metric-number">

                    {escape(str(score))}

                </div>

                <div class="metric-description">

                    Overall Business Health

                </div>

            </div>

            <div class="metric-box">

                <div class="metric-label">

                    AI CONFIDENCE

                </div>

                <div class="metric-number">

                    {escape(str(confidence))}%

                </div>

                <div class="metric-description">

                    Confidence in Analysis

                </div>

            </div>

        </div>

        <div class="priority-wrapper">

            <div class="priority-title">

                Priority Status

            </div>

            <div class="priority-pill">

                🟠 {escape(str(priority))}

            </div>

        </div>

    </div>

</div>

"""

    return html
