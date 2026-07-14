import streamlit as st

# =====================================================
# PAGE
# =====================================================

def show_executive(result):

    ai = result.ai_report or {}

    st.title("📊 Executive Intelligence Report")

    show_header(result)

    st.divider()

    show_health_snapshot(ai)

    st.divider()

    show_business_brief(ai)

    st.divider()

    show_executive_summary(ai)

    st.divider()

    show_diagnosis(ai)

    st.divider()

    show_key_findings(ai)

    # Remaining sections will be added in Part 2


# =====================================================
# HEADER
# =====================================================

def show_header(result):

    st.subheader("Executive Intelligence Brief")

    col1, col2 = st.columns(2)

    with col1:

        st.caption(f"Company : {result.company_name}")

        st.caption(f"Project : {result.project_name}")

    with col2:

        st.caption(
            f"Reporting Period : {result.metadata.get('reporting_period','-')}"
        )

        st.caption(
            f"Analysis ID : {result.analysis_id}"
        )


# =====================================================
# HEALTH SNAPSHOT
# =====================================================

def show_health_snapshot(ai):

    health = ai.get("health_snapshot", {})

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Business Health",
            health.get("status", "-"),
        )

    with c2:

        st.metric(
            "Health Score",
            health.get("score", "-"),
        )

    with c3:

        st.metric(
            "AI Confidence",
            f"{health.get('confidence',0)}%",
        )

    st.info(

        health.get(

            "management_priority",

            "No management priority identified."

        )

    )


# =====================================================
# BUSINESS BRIEF
# =====================================================

def show_business_brief(ai):

    st.subheader("📌 Business Brief")

    st.write(

        ai.get(

            "business_brief",

            "Business Brief unavailable."

        )

    )


# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

def show_executive_summary(ai):

    st.subheader("📑 Executive Summary")

    st.write(

        ai.get(

            "executive_summary",

            "Executive Summary unavailable."

        )

    )


# =====================================================
# COMMERCIAL DIAGNOSIS
# =====================================================

def show_diagnosis(ai):

    st.subheader("🩺 Commercial Diagnosis")

    st.write(

        ai.get(

            "diagnosis",

            "Diagnosis unavailable."

        )

    )


# =====================================================
# KEY FINDINGS
# =====================================================

def show_key_findings(ai):

    st.subheader("🔍 Key Findings")

    findings = ai.get("key_findings", [])

    if len(findings) == 0:

        st.info("No findings available.")

        return

    severity_icon = {

        "Critical": "🔴",

        "High": "🟠",

        "Medium": "🟡",

        "Low": "🟢",

    }

    for finding in findings:

        icon = severity_icon.get(

            finding.get("severity", "Medium"),

            "⚪",

        )

        with st.container(border=True):

            st.markdown(

                f"### {icon} {finding.get('title','Finding')}"

            )

            st.markdown(

                f"**Severity :** {finding.get('severity','Medium')}"

            )

            st.write(

                finding.get(

                    "insight",

                    "No insight available."

                )

            )

            evidence = finding.get(

                "evidence",

                ""

            )

            if evidence:

                st.caption(

                    f"Evidence : {evidence}"

                )
