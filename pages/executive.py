import streamlit as st


# =====================================================
# PAGE
# =====================================================

def show_executive(result):
    

    st.title("📊 Executive Intelligence Report")


    

    ai = result.ai_report or {}

    show_header(result)

    st.divider()

    show_health_snapshot(ai)

    st.divider()

    show_business_brief(ai)

    st.divider()

    show_executive_summary(ai)
    # STOP HERE FOR NOW


# =====================================================
# HEADER
# =====================================================

def show_header(result):

    st.subheader("📊 Executive Intelligence Brief")

    st.caption(
        f"{result.company_name} | {result.project_name}"
    )

    st.caption(
        f"Reporting Period : {result.metadata['reporting_period']}"
    )


# =====================================================
# HEALTH SNAPSHOT
# =====================================================

def show_health_snapshot(ai):

    health = ai.get("health_snapshot", {})

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Business Health", health.get("status", "Pending"))

    with col2:
        st.metric("Health Score", health.get("score", "--"))

    with col3:
        st.metric("Confidence", f"{health.get('confidence', 0)}%")

    st.info(
        "**Primary Management Focus**\n\n"
        + health.get(
            "management_priority",
            "Awaiting AI analysis."
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
            "Awaiting AI analysis."
        )
    )


# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

def show_executive_summary(ai):

    st.divider()

    show_key_findings(ai)
    
    st.divider()
    
    show_root_causes(ai)
    
    st.divider()
    
    show_risks(ai)
    
    st.divider()
    
    show_opportunities(ai)
    
    st.divider()
    
    show_recommendations(ai)
    
    st.divider()
    
    show_monday_plan(ai)
    
    st.divider()
    
    show_leadership_questions(ai)

    st.subheader("📑 Executive Summary")

    st.write(
        ai.get(
            "executive_summary",
            "Awaiting AI analysis."
        )
    )
