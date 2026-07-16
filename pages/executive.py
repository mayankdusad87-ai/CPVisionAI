import streamlit as st

# =====================================================
# PAGE
# =====================================================

# ----------------------------------------------------
# Hidden for MVP v1
# These sections will return once supported by
# Business Intelligence Signals instead of AI inference.
# ----------------------------------------------------

def show_executive(result):

    ai = result.ai_report or {}

    st.title("📊 Executive Intelligence Report")

    show_header(result)

    st.divider()

    show_health_snapshot(ai)
    
    st.divider()
    
    show_executive_highlights(ai)
    
    st.divider()

    show_commercial_intelligence(result)

    st.divider()

    show_health_snapshot(ai)

    st.divider()

    #show_business_brief(ai)

    #st.divider()

    #show_executive_summary(ai)

    #st.divider()

    #show_diagnosis(ai)

    st.divider()

    show_key_findings(ai)

    #st.divider()

    #show_root_causes(ai)

    #st.divider()

    #show_risks(ai)

    #st.divider()

    #show_opportunities(ai)

    st.divider()

    show_recommendations(ai)

    st.divider()

    show_monday_plan(ai)

    st.divider()

    show_leadership_questions(ai)   
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
# COMMERCIAL INTELLIGENCE
# =====================================================

def show_commercial_intelligence(result):

    signal = result.metadata.get(
        "commercial_intelligence",
        {},
    )

    if not signal:

        return

    st.subheader("🏢 Commercial Intelligence")

    col1, col2 = st.columns([1, 3])

    with col1:

        severity = signal.get("severity", "Unknown")

        status_icon = {
            "Excellent": "🟢",
            "Low": "🟡",
            "Medium": "🟠",
            "Critical": "🔴",
        }

        icon = status_icon.get(
            severity,
            "⚪",
        )

        st.metric(
            "Business Status",
            f"{icon} {severity}",
        )

    with col2:

        st.markdown(
            f"### {signal.get('title','Commercial Intelligence')}"
        )

        st.write(
            signal.get(
                "summary",
                "",
            )
        )

    evidence = signal.get(
        "evidence",
        {},
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Overall Conversion",
            f"{evidence.get('overall_conversion',0)}%",
        )

    with c2:

        st.metric(
            "CP Conversion",
            f"{evidence.get('cp_conversion',0)}%",
        )

    with c3:

        st.metric(
            "Conversion Gap",
            f"{evidence.get('conversion_gap',0)}%",
        )

    st.info(

        "**Business Impact**\n\n"

        + signal.get(

            "business_impact",

            "",

        )

    )

    st.warning(

        "**Management Question**\n\n"

        + signal.get(

            "management_question",

            "",

        )

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

def show_executive_highlights(ai):

    st.subheader("⭐ Executive Intelligence Highlights")

    highlights = ai.get("executive_highlights", [])

    if not highlights:
        st.info("No Executive Intelligence Highlights available.")
        return

    severity_icon = {
        "Critical": "🔴",
        "High": "🟠",
        "Medium": "🟡",
        "Low": "🟢",
        "Excellent": "🟢",
    }

    for item in highlights:

        icon = severity_icon.get(
            item.get("priority", "Medium"),
            "⚪"
        )

        with st.container(border=True):

            st.markdown(
                f"### {icon} {item.get('title', 'Executive Insight')}"
            )

            st.markdown("**Observation**")
            st.write(
                item.get("observation", "")
            )

            evidence = item.get("evidence", {})

            if evidence:

                st.markdown("**Evidence**")

                for metric, value in evidence.items():

                    st.write(
                        f"• **{metric.replace('_',' ').title()}** : {value}"
                    )

            implication = item.get(
                "business_implication",
                ""
            )

            if implication:

                st.markdown("**Business Implication**")

                st.write(
                    implication
                )

            action = item.get(
                "management_action",
                ""
            )

            if action:

                st.markdown("**Management Action**")

                st.write(
                    action
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
# =====================================================
# MANAGEMENT RECOMMENDATIONS
# =====================================================

def show_recommendations(ai):

    st.subheader("🎯 Management Recommendations")

    recommendations = ai.get("recommendations", [])

    if not recommendations:

        st.info("No recommendations available.")

        return

    priority_color = {

        "High": "🔴",

        "Medium": "🟠",

        "Low": "🟢",

    }

    for rec in recommendations:

        priority = rec.get("priority", "Medium")

        icon = priority_color.get(priority, "⚪")

        with st.container(border=True):

            st.markdown(
                f"### {icon} Priority : {priority}"
            )

            st.write(
                f"**Recommendation** : {rec.get('action','-')}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.caption(
                    f"Owner : {rec.get('owner','-')}"
                )

            with col2:

                st.caption(
                    f"Timeline : {rec.get('timeline','-')}"
                )
# =====================================================
# MONDAY MORNING ACTION PLAN
# =====================================================

def show_monday_plan(ai):

    st.subheader("📅 Monday Morning Action Plan")

    plan = ai.get("monday_plan", [])

    if not plan:

        st.info("No immediate action plan available.")

        return

    for index, task in enumerate(plan, start=1):

        st.checkbox(

            f"Action {index} : {task}",

            value=False,

            disabled=True,

        )
# =====================================================
# LEADERSHIP QUESTIONS
# =====================================================

def show_leadership_questions(ai):

    st.subheader("💬 Questions for Leadership")

    questions = ai.get("leadership_questions", [])

    if not questions:

        st.info("No leadership questions available.")

        return

    for question in questions:

        st.markdown(

            f"- {question}"

        )
