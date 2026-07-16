"""
=========================================================
ChannelIQ

Badges

=========================================================
"""

import streamlit as st


def priority_badge(text):

    st.markdown(

        f"""

<div class="priority-pill">

{text}

</div>

""",

        unsafe_allow_html=True,

    )
