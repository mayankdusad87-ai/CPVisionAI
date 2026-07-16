"""
=========================================================
ChannelIQ

Executive Workspace

=========================================================
"""

import streamlit as st


class ExecutiveWorkspace:

    def render(self, result, ai):

        health = ai.get("health_snapshot", {})

        reporting_period = result.metadata.get(
            "reporting_period",
            "-",
        )

        analysis_id = result.analysis_id

        status = health.get("status", "-")
        score = health.get("score", "-")
        confidence = health.get("confidence", 0)
        priority = health.get(
            "management_priority",
            "No Priority",
        )

        # --------------------------------------------------
        # Header
        # --------------------------------------------------

        st.markdown(
            """
            <div class="executive-wrapper">

                <div class="executive-card">

                    <div class="executive-top">

                        <div>

                            <div class="executive-title">
                                📊 Executive Intelligence Report
                            </div>

                            <div class="executive-subtitle">
                                AI Powered Business Intelligence
                            </div>

                        </div>

                        <div class="metadata-card">

                            <div class="meta-label">
                                REPORTING PERIOD
                            </div>

                            <div class="meta-value">
            """
            + str(reporting_period)
            + """
                            </div>

                            <div class="meta-label">
                                ANALYSIS ID
                            </div>

                            <div class="meta-value">
            """
            + str(analysis_id)
            + """
                            </div>

                        </div>

                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### Executive Intelligence Brief")

        st.write("")

        # --------------------------------------------------
        # KPI Tiles
        # --------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(
                f"""
<div class="metric-box">

<div class="metric-label">

SENTIMENT

</div>

<div class="metric-number">

{status}

</div>

<div class="metric-description">

Overall Business Outlook

</div>

</div>
""",
                unsafe_allow_html=True,
            )

        with col2:

            st.markdown(
                f"""
<div class="metric-box">

<div class="metric-label">

HEALTH SCORE

</div>

<div class="metric-number">

{score}

</div>

<div class="metric-description">

Overall Business Health

</div>

</div>
""",
                unsafe_allow_html=True,
            )

        with col3:

            st.markdown(
                f"""
<div class="metric-box">

<div class="metric-label">

AI CONFIDENCE

</div>

<div class="metric-number">

{confidence}%

</div>

<div class="metric-description">

Evidence Confidence

</div>

</div>
""",
                unsafe_allow_html=True,
            )

        st.write("")

        st.markdown(
            f"""
<div class="priority-wrapper">

<div class="priority-title">

Priority Status

</div>

<div class="priority-pill">

🟠 {priority}

</div>

</div>
""",
            unsafe_allow_html=True,
        )

        st.divider()

        st.subheader("Executive Intelligence Highlights")

        st.info(
            "Executive Highlights will be connected in the next step."
        )

        st.divider()

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "Executive",
                "Commercial",
                "Insights",
                "Recommendations",
                "Action Plan",
            ]
        )

        with tab1:
            st.write("Executive View")

        with tab2:
            st.write("Commercial Intelligence")

        with tab3:
            st.write("Insights")

        with tab4:
            st.write("Recommendations")

        with tab5:
            st.write("Action Plan")
