import streamlit as st


def show_partner_page(result):
    st.title("PARTNER PAGE LOADED")

    st.write(result)

    st.header("🏆 Partner Intelligence")

    partner_table = result.metadata["partner_table"]

    st.dataframe(
        partner_table,
        use_container_width=True,
        hide_index=True,
    )
