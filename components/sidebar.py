import streamlit as st


def show_sidebar():
    """Display the application sidebar."""

    with st.sidebar:

        st.markdown("## 🌍 AI Language Translator")
        st.caption("Version 1.0")

        st.divider()

        st.markdown("""
        <div style="
            background:#F8FAFC;
            border:1px solid #E5E7EB;
            border-radius:12px;
            padding:15px;
            margin-bottom:15px;
        ">

        <h4 style="
            color:#2563EB;
            margin-top:0;
            margin-bottom:15px;
        ">
        ✨ Features
        </h4>

        <p style="margin:10px 0;">🌐 AI-Powered Translation</p>

        <p style="margin:10px 0;">🌍 20+ Languages</p>

        <p style="margin:10px 0;">🔊 Text-to-Speech</p>

        <p style="margin:10px 0;">📥 Download Translation</p>

        <p style="margin:10px 0;">📜 Translation History</p>

        <p style="margin:10px 0;">📊 Analytics Dashboard</p>

        </div>
        """, unsafe_allow_html=True)

        st.success("✅ Ready to Translate")