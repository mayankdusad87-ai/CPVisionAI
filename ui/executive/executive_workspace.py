"""
=========================================================

ChannelIQ

Executive Workspace

=========================================================
"""

import streamlit as st

from ui.components.header import Header
from ui.components.metric_card import MetricCard
from ui.components.badge import Badge
from ui.components.tabs import WorkspaceTabs


class ExecutiveWorkspace:

    def render(

        self,

        result,

        ai,

    ):

        Header.render(

            "Executive Intelligence Workspace",

            "OFFICIAL EXECUTIVE INTELLIGENCE BRIEFING",

        )

        st.markdown("<br>", unsafe_allow_html=True)

        self.executive_brief(

            result,

            ai,

        )

    # =====================================================

    # Executive Brief

    # =====================================================

    def executive_brief(

        self,

        result,

        ai,

    ):

        health = ai.get(

            "health_snapshot",

            {},

        )

        st.markdown(

            '<div class="channel-card">',

            unsafe_allow_html=True,

        )

        left, right = st.columns(

            [3,1]

        )

        with left:

            st.markdown(

                "### Executive Intelligence Brief"

            )

            st.caption(

                "OFFICIAL INTELLIGENCE BRIEFING"

            )

        with right:

            st.caption(

                "Reporting Period"

            )

            st.write(

                result.metadata.get(

                    "reporting_period",

                    "-",

                )

            )

            st.caption(

                "Analysis ID"

            )

            st.write(

                result.analysis_id

            )

        st.markdown("---")

        c1, c2, c3 = st.columns(3)

        with c1:

            MetricCard.render(

                "Health Score",

                 health.get("score","-"),

                "Overall Business Health",

                      "❤️"

            

            )

        with c2:

            MetricCard.render(

                "Health Score",

                health.get(

                    "score",

                    "-",

                ),

            )

        with c3:

            MetricCard.render(

                "AI Confidence",

                str(

                    health.get(

                        "confidence",

                        0,

                    )

                ) + "%",

            )

        st.markdown("<br>", unsafe_allow_html=True)

        Badge.priority(

            health.get(

                "management_priority",

                "No Priority",

            )

        )

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4, tab5 = WorkspaceTabs.render()

        with tab1:

            st.info(

                "Executive Highlights will be rendered here."

            )

        with tab2:

            st.info(

                "Commercial Intelligence"

            )

        with tab3:

            st.info(

                "Business Findings"

            )

        with tab4:

            st.info(

                "Recommendations"

            )

        with tab5:

            st.info(

                "Action Plan"

            )
