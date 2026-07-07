"""
Professional KPI Cards
ChannelIQ AI
"""

import streamlit as st


def metric_card(
    title: str,
    value: str,
    change: str = "",
    change_type: str = "neutral",
    subtitle: str = "",
    icon: str = "📊"
):
    """
    Render a professional KPI card.

    change_type:
        success
        danger
        warning
        neutral
    """

    colors = {
        "success": "#10B981",
        "danger": "#EF4444",
        "warning": "#F59E0B",
        "neutral": "#64748B"
    }

    arrows = {
        "success": "▲",
        "danger": "▼",
        "warning": "▲",
        "neutral": ""
    }

    color = colors.get(change_type, "#64748B")
    arrow = arrows.get(change_type, "")

    html = f"""
    <div class="metric-card">

        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            margin-bottom:18px;
        ">

            <div class="metric-title">
                {title}
            </div>

            <div style="font-size:26px;">
                {icon}
            </div>

        </div>

        <div class="metric-value">
            {value}
        </div>

        <div
            style="
            color:{color};
            font-weight:600;
            margin-top:10px;
            ">

            {arrow} {change}

        </div>

        <div
            style="
            color:#94A3B8;
            font-size:13px;
            margin-top:6px;
            ">

            {subtitle}

        </div>

    </div>
    """

    st.markdown(
        html,
        unsafe_allow_html=True
    )
