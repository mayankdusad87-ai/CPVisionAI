"""
=========================================================
ChannelIQ

Metric Card

=========================================================
"""

import streamlit as st


class MetricCard:

    @staticmethod
    def render(

        title,

        value,

        subtitle="",

        icon="",

    ):

        st.markdown(

            f"""
<div class="metric-card">

<div class="metric-title">

{icon} {title}

</div>

<div class="metric-value">

{value}

</div>

<div class="channel-subtitle">

{subtitle}

</div>

</div>

""",

            unsafe_allow_html=True,

        )
