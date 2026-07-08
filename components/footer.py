import streamlit as st


def show_footer():
    """Display application footer."""

    st.divider()

    left, center, right = st.columns([1, 3, 1])

    with center:
        st.markdown(
            "<h2 style='text-align:center; color:#2563EB;'>🌍 AI Language Translator</h2>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p style='text-align:center; color:#6B7280; font-size:16px;'>Developed by Muhammad Imran ❤️</p>",
            unsafe_allow_html=True,
        )