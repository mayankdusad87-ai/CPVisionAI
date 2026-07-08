"""
=========================================================
ChannelIQ AI

Application Entry Point

Version : 2.0
=========================================================
"""

from pathlib import Path

import streamlit as st

from config import (
    APP_NAME,
    PAGE_ICON,
    PAGE_TITLE,
    LAYOUT,
    INITIAL_SIDEBAR_STATE,
    STYLE_FILE,
)

from database import create_tables

from core.analysis_service import AnalysisService

from components.header import render_header
from components.sidebar import render_sidebar
from components.metric_cards import metric_card


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE,
)

# =========================================================
# CSS
# =========================================================

if Path(STYLE_FILE).exists():

    with open(STYLE_FILE, "r", encoding="utf-8") as css:

        st.markdown(

            f"<style>{css.read()}</style>",

            unsafe_allow_html=True,

        )

# =========================================================
# DATABASE
# =========================================================

create_tables()

# =========================================================
# SESSION STATE
# =========================================================

if "analysis_result" not in st.session_state:

    st.session_state.analysis_result = None

if "company" not in st.session_state:

    st.session_state.company = ""

if "project" not in st.session_state:

    st.session_state.project = ""

if "analysis_id" not in st.session_state:

    st.session_state.analysis_id = ""


# =========================================================
# SIDEBAR
# =========================================================

selected_page = render_sidebar()

# =========================================================
# HEADER
# =========================================================

render_header(

    company_name=st.session_state.company,

    project_name=st.session_state.project,

    analysis_id=st.session_state.analysis_id,

)

# =========================================================
# DASHBOARD
# =========================================================

if selected_page == "🏠 Dashboard":

    st.title("Executive Dashboard")

    # -----------------------------------------------------

    uploaded_file = st.file_uploader(

        "Upload Monthly Walk-in Tracker",

        type=["xlsx", "xls"],

    )

    col1, col2 = st.columns(2)

    with col1:

        company = st.text_input(

            "Company Name",

            value=st.session_state.company,

        )

        project = st.text_input(

            "Project Name",

            value=st.session_state.project,

        )

    with col2:

        month = st.selectbox(

            "Month",

            [

                "January",

                "February",

                "March",

                "April",

                "May",

                "June",

                "July",

                "August",

                "September",

                "October",

                "November",

                "December",

            ],

        )

        year = st.number_input(

            "Year",

            min_value=2020,

            max_value=2100,

            value=2026,

        )

    analyse = st.button(

        "🚀 Analyse",

        use_container_width=True,

    )

    # =====================================================
    # RUN ANALYSIS
    # =====================================================

    if analyse:

        if uploaded_file is None:

            st.error(

                "Please upload an Excel file."

            )

        else:

            with st.spinner(

                "Analysing Excel..."

            ):

                try:

                    service = AnalysisService()

                    result = service.analyse(

                        excel_file=uploaded_file,

                        company_name=company,

                        project_name=project,

                        month=month,

                        year=int(year),

                    )

                    st.session_state.analysis_result = result

                    st.session_state.company = company

                    st.session_state.project = project

                    st.session_state.analysis_id = (

                        result.analysis_id

                    )

                    st.success(

                        "Analysis completed."

                    )

                except Exception as e:

                    st.exception(e)

    # =====================================================
    # SHOW KPI
    # =====================================================

    result = st.session_state.analysis_result

    if result:

        st.divider()

        dashboard = result.metadata

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            metric_card(

                title="Fresh Walk-ins",

                value=str(

                    dashboard["fresh_walkins"]

                ),

                change="",

                change_type="neutral",

                subtitle="Current Month",

                icon="🚶",

            )

        with c2:

            metric_card(

                title="Bookings",

                value=str(

                    result.total_bookings

                ),

                change="",

                change_type="neutral",

                subtitle="Current Month",

                icon="🏠",

            )

        with c3:

            metric_card(

                title="Booking %",

                value=f"{result.conversion}%",

                change="",

                change_type="neutral",

                subtitle="Current Month",

                icon="🎯",

            )

        with c4:

            metric_card(

                title="Active Partners",

                value=str(

                    dashboard["active_channel_partners"]

                ),

                change="",

                change_type="neutral",

                subtitle="Last 30 Days",

                icon="🤝",

            )

        st.divider()

        st.subheader(

            "Executive Summary"

        )

        st.info(

            result.executive_summary

        )

        st.subheader(

            "Recommendations"

        )

        for item in result.recommendations:

            st.write("•", item)

    else:

        st.info(

            "Upload an Excel file and click Analyse."

        )

# =========================================================
# OTHER PAGES
# =========================================================

else:

    st.info(

        f"{selected_page} will be implemented in upcoming sprints."

    )
