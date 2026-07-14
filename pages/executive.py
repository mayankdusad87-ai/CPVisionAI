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

    st.divider()
    
    show_root_causes(ai)
    
    st.divider()
    
    show_risks(ai)
    
    st.divider()
    
    show_opportunities(ai)

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
# =====================================================
# ROOT CAUSES
# =====================================================

def show_root_causes(ai):

    st.subheader("🧩 Root Causes")

    causes = ai.get("root_causes", [])

    if not causes:

        st.info("No root causes identified.")

        return

    for cause in causes:

        with st.container(border=True):

            st.markdown(
                f"### {cause.get('cause','Unknown Cause')}"
            )

            st.write(
                cause.get(
                    "business_impact",
                    "No business impact available."
                )
            )


# =====================================================
# BUSINESS RISKS
# =====================================================

def show_risks(ai):

    st.subheader("⚠ Business Risks")

    risks = ai.get("risks", [])

    if not risks:

        st.success("No significant risks identified.")

        return

    severity_icons = {

        "Critical": "🔴",

        "High": "🟠",

        "Medium": "🟡",

        "Low": "🟢",

    }

    for risk in risks:

        severity = risk.get("severity", "Medium")

        icon = severity_icons.get(severity, "⚪")

        with st.container(border=True):

            st.markdown(
                f"### {icon} {risk.get('risk','Business Risk')}"
            )

            st.markdown(
                f"**Severity :** {severity}"
            )

            st.write(
                risk.get(
                    "mitigation",
                    "No mitigation available."
                )
            )


# =====================================================
# OPPORTUNITIES
# =====================================================

def show_opportunities(ai):

    st.subheader("🚀 Business Opportunities")

    opportunities = ai.get("opportunities", [])

    if not opportunities:

        st.info("No opportunities identified.")

        return

    for opportunity in opportunities:

        with st.container(border=True):

            st.markdown(
                f"### {opportunity.get('opportunity','Opportunity')}"
            )

            st.markdown(
                f"**Potential Impact :** {opportunity.get('impact','-')}"
            )

            st.write(
                opportunity.get(
                    "recommended_action",
                    "No recommendation available."
                )
            )
