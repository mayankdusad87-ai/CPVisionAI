"""
=========================================================
ChannelIQ

Badge Component

=========================================================
"""

import streamlit as st


class Badge:

    @staticmethod
    def priority(text):

        st.markdown(

            f"""

<div class="priority-pill">

{text}

</div>

""",

            unsafe_allow_html=True,

        )
