import streamlit as st


def show_header():
    """Display the application header."""

    st.markdown("""
    <style>

    .header-container{
        background: linear-gradient(90deg,#2563EB,#3B82F6,#60A5FA);
        padding:35px;
        border-radius:18px;
        color:white;
        text-align:center;
        margin-bottom:25px;
        box-shadow:0px 6px 18px rgba(0,0,0,0.20);
    }

    .header-title{
        font-size:42px;
        font-weight:bold;
        margin-bottom:8px;
    }

    .header-subtitle{
        font-size:20px;
        opacity:0.95;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="header-container">

    <div class="header-title">
    🌍 AI Language Translator
    </div>

    <div class="header-subtitle">
    Translate any language instantly with AI-powered translation
    </div>

    </div>
    """, unsafe_allow_html=True)