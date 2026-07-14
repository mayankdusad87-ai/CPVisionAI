import streamlit as st


def show_executive(result):

    st.header("📈 Executive Report")

    st.subheader("Business Brief")

    st.info(
        result.ai_report.get(
            "business_brief",
            "No Business Brief"
        )
    )

    st.subheader("Executive Summary")

    st.write(
        result.executive_summary
    )

    st.subheader("Recommendations")

    for item in result.recommendations:

        st.write("•", item)
