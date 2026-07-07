"""
Sidebar Component
"""

import streamlit as st


MENU = [
    "🏠 Dashboard",
    "📈 Executive Report",
    "🏆 Partner Intelligence",
    "⚠ Risk Center",
    "🚀 Opportunity Center",
    "📊 Trends",
    "🤖 AI Consultant",
    "📤 Export",
    "⚙ Settings",
]


def render_sidebar():

    with st.sidebar:

        st.markdown("## ChannelIQ AI")

        st.caption("Enterprise Edition")

        st.divider()

        page = st.radio(
            "Navigation",
            MENU,
            label_visibility="collapsed",
        )

        st.divider()

        st.markdown("### Recent Analysis")

        st.info(
            """
            No analysis selected.
            Upload a file to begin.
            """
        )

        st.divider()

        st.caption("Version 2.0")

    return page
