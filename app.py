"""
=========================================================
ChannelIQ AI

Application Entry Point

Enterprise Architecture V2.2
=========================================================
"""

from pathlib import Path

import streamlit as st

# =========================================================
# CONFIG
# =========================================================

from config import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    INITIAL_SIDEBAR_STATE,
    STYLE_FILE,
)

# =========================================================
# DATABASE
# =========================================================

from database import create_tables

# =========================================================
# CORE
# =========================================================

from core.analysis_service import AnalysisService
from core.excel_reader import ExcelReader
from core.reporting_period import ReportingPeriod

# =========================================================
# COMPONENTS
# =========================================================

from components.header import render_header
from components.sidebar import render_sidebar

# =========================================================
# PAGES
# =========================================================

from pages.dashboard import show_dashboard
from pages.executive import show_executive
from pages.partner_intelligence import show_partner_page

# Future Pages
# from pages.risk import show_risk
# from pages.opportunity import show_opportunity
# from pages.trends import show_trends
# from pages.consultant import show_consultant


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

def initialise_session():

    defaults = {

        "analysis_result": None,

        "analysis_id": "",

        "company": "",

        "project": "",

        "uploaded_file": None,

        "full_dataframe": None,

        "available_periods": [],

        "selected_period": None,

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


initialise_session()

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
# DASHBOARD PAGE
# =========================================================

if selected_page == "🏠 Dashboard":

    st.title("Executive Dashboard")

    st.caption(
        "AI-powered Channel Partner Performance Intelligence"
    )

    st.divider()
    # =========================================================
    # UPLOAD SECTION
    # =========================================================
    
    st.subheader("📂 Upload Monthly Tracker")
    
    uploaded_file = st.file_uploader(
        "Upload ChannelIQ Excel Tracker",
        type=["xlsx", "xls"],
        help="Upload the latest Channel Partner tracker.",
    )
    
    # =========================================================
    # READ EXCEL
    # =========================================================
    
    if uploaded_file is not None:
    
        file_changed = (
    
            st.session_state.uploaded_file is None
    
            or
    
            uploaded_file.name
            != st.session_state.uploaded_file.name
    
        )
    
        if file_changed:
    
            try:
    
                with st.spinner(
                    "Reading Excel Tracker..."
                ):
    
                    reader = ExcelReader()
    
                    full_df = reader.read(
                        uploaded_file
                    )
    
                    reporting = ReportingPeriod()
    
                    periods = reporting.available_periods(
                        full_df
                    )
    
                    latest = reporting.latest_period(
                        full_df
                    )
    
                    # -----------------------------
                    # SESSION
                    # -----------------------------
    
                    st.session_state.uploaded_file = uploaded_file
    
                    st.session_state.full_dataframe = full_df
    
                    st.session_state.available_periods = periods
    
                    st.session_state.selected_period = latest
    
                    # Reset previous analysis
    
                    st.session_state.analysis_result = None
    
                st.success(
                    f"Tracker loaded successfully "
                    f"({len(full_df):,} records)"
                )
    
            except Exception as ex:
    
                st.error(
                    "Unable to read uploaded tracker."
                )
    
                st.exception(ex)
    
        # =========================================================
        # DATASET SUMMARY
        # =========================================================
        
        if st.session_state.full_dataframe is not None:
            st.write("Selected Page:", selected_page)
            st.write("Analysis Result Exists:", st.session_state.analysis_result is not None)
        
            st.divider()
        
            st.subheader("Dataset Summary")
        
            c1, c2, c3 = st.columns(3)
        
            with c1:
        
                st.metric(
        
                    "Total Records",
        
                    len(
                        st.session_state.full_dataframe
                    ),
        
                )
        
            with c2:
        
                st.metric(
        
                    "Reporting Periods",
        
                    len(
                        st.session_state.available_periods
                    ),
        
                )
        
            with c3:
        
                st.metric(
        
                    "Latest Period",
        
                    st.session_state.selected_period,
        
                ) 
                
        # =========================================================
        # ANALYSIS SETTINGS
        # =========================================================
        
        if st.session_state.full_dataframe is not None:
        
            st.divider()
        
            st.subheader("⚙ Analysis Settings")
        
            left, right = st.columns(2)

        # -----------------------------------------------------
        # COMPANY / PROJECT
        # -----------------------------------------------------
    
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
    
        # -----------------------------------------------------
        # REPORTING PERIOD
        # -----------------------------------------------------
    
        with right:
    
            selected_period = st.selectbox(
                "Analysis Period",
                options=st.session_state.available_periods,
                index=st.session_state.available_periods.index(
                    st.session_state.selected_period
                ),
            )
    
        # -----------------------------------------------------
        # SAVE SESSION
        # -----------------------------------------------------
    
        st.session_state.company = company
    
        st.session_state.project = project
    
        st.session_state.selected_period = selected_period
    
        st.divider()
    
        # =====================================================
        # ANALYSE BUTTON
        # =====================================================
    
        if st.button(
            "🚀 Analyse",
            use_container_width=True,
            type="primary",
        ):
    
            try:
    
                with st.spinner(
                    "Generating Executive Intelligence..."
                ):
    
                    service = AnalysisService()
    
                    result = service.analyse(
    
                        dataframe=st.session_state.full_dataframe,
    
                        company_name=company,
    
                        project_name=project,
    
                        reporting_period=selected_period,
    
                    )
    
                    # --------------------------------------
                    # SAVE SESSION
                    # --------------------------------------
    
                    st.session_state.analysis_result = result
    
                    st.session_state.analysis_id = result.analysis_id
    
                    st.success(
                        "Analysis completed successfully."
                    )
    
            except Exception as ex:
    
                st.exception(ex)
       
    if st.session_state.analysis_result:
    
        result = st.session_state.analysis_result
    
        PAGE_ROUTES = {
    
            "🏠 Dashboard": show_dashboard,
    
            "📈 Executive Report": show_executive,
    
            "🏆 Partner Intelligence": show_partner_page,
    
        }
    
        PAGE_ROUTES[selected_page](result)
