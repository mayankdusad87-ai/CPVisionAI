"""
=========================================================
ChannelIQ AI
Application Entry Point
Sprint 1.1
=========================================================
"""

from pathlib import Path

import streamlit as st

from config import (
    APP_NAME,
    APP_TAGLINE,
    PAGE_ICON,
    PAGE_TITLE,
    LAYOUT,
    INITIAL_SIDEBAR_STATE,
    STYLE_FILE,
)

from database import (
    DatabaseConnection,
    create_tables,
)

from components.header import render_header
from components.sidebar import render_sidebar
from components.metric_cards import metric_card


# --------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE,
)

# --------------------------------------------------------
# LOAD CSS
# --------------------------------------------------------

if Path(STYLE_FILE).exists():
    with open(STYLE_FILE, "r", encoding="utf-8") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )

# --------------------------------------------------------
# DATABASE
# --------------------------------------------------------

create_tables()

# --------------------------------------------------------
# SESSION STATE
# --------------------------------------------------------

DEFAULT_STATE = {
    "company": None,
    "project": None,
    "analysis_id": None,
}

for key, value in DEFAULT_STATE.items():
    st.session_state.setdefault(key, value)

# --------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------

selected_page = render_sidebar()

# --------------------------------------------------------
# HEADER
# --------------------------------------------------------

render_header(
    company_name=st.session_state.company,
    project_name=st.session_state.project,
    analysis_id=st.session_state.analysis_id,
)

# --------------------------------------------------------
# DASHBOARD
# --------------------------------------------------------

if selected_page == "🏠 Dashboard":

    st.markdown("## Executive Dashboard")

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:

        st.info(
            """
            Welcome to **ChannelIQ AI**.

            Upload your monthly Channel Partner Tracker
            to generate executive insights.
            """
        )

    with col2:

        st.button(
            "➕ New Analysis",
            use_container_width=True,
        )

    with col3:

        st.button(
            "📂 History",
            use_container_width=True,
        )

    st.divider()

    k1, k2, k3 = st.columns(3)

    with k1:

        metric_card(
            title="Network Health",
            value="--",
            change="No Data",
            change_type="neutral",
            subtitle="Awaiting upload",
            icon="💚",
        )

    with k2:

        metric_card(
            title="Bookings",
            value="--",
            change="No Data",
            change_type="neutral",
            subtitle="Awaiting upload",
            icon="🏠",
        )

    with k3:

        metric_card(
            title="Conversion",
            value="--",
            change="No Data",
            change_type="neutral",
            subtitle="Awaiting upload",
            icon="🎯",
        )

    st.divider()

    left, right = st.columns([3, 2])

    with left:

       uploaded_file = st.file_uploader(
    "Upload Monthly Walk-in Tracker",
    type=["xlsx", "xls"],
)

company = st.text_input(
    "Company Name"
)

project = st.text_input(
    "Project Name"
)

month = st.selectbox(
    "Month",
    [
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
    ]
)

year = st.number_input(
    "Year",
    value=2026,
    step=1,
)

analyse = st.button(
    "🚀 Analyse",
    use_container_width=True,
)

    with right:

        st.subheader("Recent Analysis")

        st.info(
            "No analysis available yet."
        )

# --------------------------------------------------------
# PLACEHOLDER PAGES
# --------------------------------------------------------

else:

    st.info(
        f"{selected_page} will be implemented in the next sprints."
    )
