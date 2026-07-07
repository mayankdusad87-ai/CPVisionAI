"""
ChannelIQ AI
Reusable Header Component
"""

from datetime import datetime
import streamlit as st

from config import APP_NAME, APP_TAGLINE, VERSION


def render_header(
    company_name=None,
    project_name=None,
    analysis_id=None,
):
    """
    Render the application header.
    """

    col1, col2 = st.columns([4, 1])

    with col1:

        st.markdown(
            f"""
            <div class="page-title">
                {APP_NAME}
            </div>

            <div class="page-subtitle">
                {APP_TAGLINE}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            f"""
            <div style="
                text-align:right;
                color:#64748B;
                font-size:14px;
            ">

            Version<br>

            <b>{VERSION}</b>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    info1, info2, info3, info4 = st.columns(4)

    with info1:
        st.caption("Company")
        st.write(company_name or "Not Selected")

    with info2:
        st.caption("Project")
        st.write(project_name or "Not Selected")

    with info3:
        st.caption("Analysis ID")
        st.write(analysis_id or "-")

    with info4:
        st.caption("Generated On")
        st.write(datetime.now().strftime("%d %b %Y"))

    st.markdown("<br>", unsafe_allow_html=True)
