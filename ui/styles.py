"""
=========================================================
ChannelIQ

Global Style Loader

=========================================================
"""

from pathlib import Path
import streamlit as st


def _load_css(file_path: Path):

    if file_path.exists():

        st.markdown(

            f"<style>{file_path.read_text(encoding='utf-8')}</style>",

            unsafe_allow_html=True,

        )


def load_styles():

    base = Path(__file__).parent.parent

    css_folder = base / "assets" / "css"

    # Global theme
    _load_css(base / "assets" / "channeliq.css")

    # Executive page
    _load_css(css_folder / "executive.css")
