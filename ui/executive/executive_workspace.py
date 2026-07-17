"""
=========================================================
ChannelIQ AI

Executive Workspace

=========================================================
"""

import streamlit as st


class ExecutiveWorkspace:

    def render(self, result, ai):

        health = ai.get("health_snapshot", {})

        reporting_period = result.metadata.get("reporting_period", "-")
        analysis_id = result.analysis_id

        sentiment = health.get("status", "-")
        score = health.get("score", "-")
        confidence = health.get("confidence", 0)
        priority = health.get("management_priority", "Medium")

        # ------------------------------------------------
        # HEADER
        # ------------------------------------------------

        st.markdown(
            """
# 📊 Executive Intelligence Report

AI Powered Business Intelligence
"""
        )

        st.divider()

        left, right = st.columns([3, 1])

        with left:
            st.markdown(
                """
### Executive Intelligence Brief

Official Executive Intelligence Briefing
"""
            )

        with right:
            st.info(
                f"""
**Reporting Period**

{reporting_period}

---

**Analysis ID**

{analysis_id}
"""
            )

        st.write("")

        c1, c2, c3 = st.columns(3)

        metrics = [
            ("Sentiment", sentiment),
            ("Health Score", score),
            ("AI Confidence", f"{confidence}%"),
        ]

        for col, (title, value) in zip([c1, c2, c3], metrics):
            with col:
                st.markdown(
                    f"""
<div class="metric-card">
<div class="metric-title">{title}</div>
<div class="metric-value">{value}</div>
</div>
""",
                    unsafe_allow_html=True,
                )

        st.write("")
        st.success(f"Priority Status : {priority}")
        st.divider()

        # ------------------------------------------------
        # Executive Intelligence Highlights
        # ------------------------------------------------

        st.subheader("Executive Intelligence Highlights")

        highlights = ai.get("executive_highlights", [])

        if highlights:

            for item in highlights:

                with st.container(border=True):

                    st.markdown(f"## {item.get('title', 'Executive Insight')}")
                    st.divider()

                    st.markdown("### 💡 Key Insight")
                    st.write(
                        item.get(
                            "key_insight",
                            item.get("observation", "Not Available"),
                        )
                    )

                    st.markdown("### 📊 Supporting Evidence")
                    evidence = item.get(
                        "supporting_evidence",
                        item.get("evidence", {}),
                    )
                    st.markdown("### 📊 Supporting Evidence")

                    
                    # ------------------------------------------------
                    # Evidence as List
                    # ------------------------------------------------
                    
                    if isinstance(evidence, list):
                    
                        table_data = []
                    
                        for row in evidence:
                    
                            table_data.append(
                                {
                                    "Metric": row.get("metric", ""),
                                    "Value": row.get("value", ""),
                                }
                            )
                    
                        st.table(table_data)
                    
                    # ------------------------------------------------
                    # Evidence as Dictionary
                    # ------------------------------------------------
                    
                    elif isinstance(evidence, dict):
                    
                        table_data = []
                    
                        for key, value in evidence.items():
                    
                            table_data.append(
                                {
                                    "Metric": key.replace("_", " ").title(),
                                    "Value": value,
                                }
                            )
                    
                        st.table(table_data)
                    
                    # ------------------------------------------------
                    # Anything Else
                    # ------------------------------------------------
                    
                    else:
                    
                        st.write(evidence)

                    if isinstance(evidence, dict):
                        st.table(evidence)
                    else:
                        st.write(evidence)

                    st.markdown("### 💼 Business Implication")
                    st.write(
                        item.get(
                            "business_implication",
                            "Not Available",
                        )
                    )

                    st.markdown("### 🎯 Recommended Management Action")
                    st.write(
                        item.get(
                            "recommended_management_action",
                            item.get(
                                "recommended_action",
                                "Not Available",
                            ),
                        )
                    )

                    st.write("")

        else:
            st.info("No Executive Highlights Available.")

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
            st.write(
                ai.get(
                    "executive_summary",
                    "No Executive Summary",
                )
            )

        with tab2:
            st.json(
                result.metadata.get(
                    "commercial_intelligence",
                    {},
                )
            )

        with tab3:
            st.write("Business Insights")

        with tab4:
            st.write("Recommendations")

        with tab5:
            st.write("Action Plan")
