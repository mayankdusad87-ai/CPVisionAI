"""
=========================================================
ChannelIQ AI

Application Entry Point

Version : 2.1
=========================================================
"""
from pages.dashboard import show_dashboard

from pages.executive import show_executive

from pages.partner_intelligence import show_partner_page


from pathlib import Path

import streamlit as st
from openai import OpenAI

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
from core.excel_reader import ExcelReader
from core.reporting_period import ReportingPeriod

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
# LOAD CSS
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

DEFAULT_STATE = {

    "analysis_result": None,

    "analysis_id": "",

    "company": "",

    "project": "",

    "uploaded_file": None,

    "full_dataframe": None,

    "available_periods": [],

    "selected_period": None,

}

for key, value in DEFAULT_STATE.items():

    if key not in st.session_state:

        st.session_state[key] = value

# =========================================================
# SIDEBAR
# =========================================================

selected_page = render_sidebar()

if st.sidebar.button("🧪 Test OpenAI"):

    try:

        api_key = st.secrets.get("OPENAI_API_KEY")

        client = OpenAI(api_key=api_key)

        response = client.responses.create(

            model="gpt-5-mini",

            input="Reply with exactly: SUCCESS"

        )

        st.success("✅ OpenAI Connected")

        st.code(response.output_text)

    except Exception as ex:

        st.error("❌ OpenAI Failed")

        st.exception(ex)

# =========================================================
# HEADER
# =========================================================

render_header(

    company_name=st.session_state.company,

    project_name=st.session_state.project,

    analysis_id=st.session_state.analysis_id,

)

# =========================================================
# PAGE TITLE
# =========================================================

if selected_page == "🏠 Dashboard":

    st.title("Executive Dashboard")

    st.caption(
        "AI-powered Channel Partner Performance Intelligence"
    )

    st.divider()

    


    

    # =====================================================
    # Sprint 2 starts here...
    # (Upload Section will be added in Part 2)
    # =====================================================


    # =====================================================
    # UPLOAD SECTION
    # =====================================================

    st.subheader("📂 Upload Monthly Tracker")

    uploaded_file = st.file_uploader(
        "Upload ChannelIQ Excel Tracker",
        type=["xlsx", "xls"],
        help="Upload the latest Channel Partner tracker.",
    )

    # -----------------------------------------------------
    # READ EXCEL
    # -----------------------------------------------------

    if uploaded_file is not None:

        if (
            st.session_state.uploaded_file is None
            or
            uploaded_file.name != st.session_state.uploaded_file.name
        ):

            try:

                with st.spinner("Reading Excel..."):

                    reader = ExcelReader()

                    full_df = reader.read(uploaded_file)

                    reporting = ReportingPeriod()

                    periods = reporting.available_periods(full_df)

                    latest = reporting.latest_period(full_df)

                    st.session_state.uploaded_file = uploaded_file

                    st.session_state.full_dataframe = full_df

                    st.session_state.available_periods = periods

                    st.session_state.selected_period = latest

                st.success(
                    f"Tracker loaded successfully "
                    f"({len(full_df):,} records)"
                )

            except Exception as e:

                st.error("Unable to read uploaded tracker.")

                st.exception(e)

  # =====================================================
# ANALYSIS SETTINGS
# =====================================================

analyse = False

if st.session_state.full_dataframe is not None:

    st.divider()

    st.subheader("⚙ Analysis Settings")

    left, right = st.columns(2)

    # -------------------------------------------------
    # COMPANY / PROJECT
    # -------------------------------------------------

    with left:

        company = st.text_input(
            "Company",
            value=st.session_state.company,
            placeholder="Builder Name",
        )

        project = st.text_input(
            "Project",
            value=st.session_state.project,
            placeholder="Project Name",
        )

    # -------------------------------------------------
    # REPORTING PERIOD
    # -------------------------------------------------

    with right:

        if st.session_state.available_periods:

            default_index = 0

            if (
                st.session_state.selected_period
                in st.session_state.available_periods
            ):

                default_index = (
                    st.session_state.available_periods.index(
                        st.session_state.selected_period
                    )
                )

            selected_period = st.selectbox(
                "Analysis Period",
                options=st.session_state.available_periods,
                index=default_index,
            )

        else:

            selected_period = None

            st.warning(
                "No reporting periods found in the uploaded tracker."
            )

        st.caption(
            "Latest available reporting period is selected automatically."
        )

    # -------------------------------------------------
    # SAVE SESSION
    # -------------------------------------------------

    st.session_state.company = company
    st.session_state.project = project
    st.session_state.selected_period = selected_period

    # -------------------------------------------------
    # DATASET SUMMARY
    # -------------------------------------------------

    info1, info2, info3 = st.columns(3)

    with info1:

        st.metric(
            "Total Records",
            f"{len(st.session_state.full_dataframe):,}",
        )

    with info2:

        st.metric(
            "Reporting Periods",
            len(st.session_state.available_periods),
        )

    with info3:

        st.metric(
            "Selected Period",
            selected_period if selected_period else "-",
        )

    st.divider()

    analyse = st.button(
        "🚀 Analyse",
        use_container_width=True,
        type="primary",
    )
    # =====================================================
    # RUN ANALYSIS
    # =====================================================

    if analyse:

        try:

            with st.spinner("Generating Executive Dashboard..."):

                service = AnalysisService()

                result = service.analyse(

                    dataframe=st.session_state.full_dataframe,

                    company_name=company,

                    project_name=project,

                    reporting_period=selected_period,

                )

                st.session_state.analysis_result = result

                st.session_state.company = company

                st.session_state.project = project

                st.session_state.analysis_id = result.analysis_id

                st.success("Analysis completed successfully.")
            
            st.rerun()

        except Exception as e:

            st.exception(e)




        # =====================================================
        # EXECUTIVE DASHBOARD
        # =====================================================
        if st.session_state.analysis_result is not None:
        
            result = st.session_state.analysis_result
        
            if selected_page == "🏠 Dashboard":
        
                show_dashboard(result)
        
            elif selected_page == "📈 Executive Report":
        
                show_executive(result)
        
            elif selected_page == "🏆 Partner Intelligence":
        
                show_partner_page(result)
        
            else:
        
                st.info("Coming Soon")
