import streamlit as st

from components.sidebar import show_sidebar
from components.header import show_header
from components.cards import show_cards
from components.translator_ui import show_translator
from components.footer import show_footer
from analytics import show_analytics


def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Custom CSS
load_css()

# Sidebar
show_sidebar()

# Header
show_header()

# Feature Cards
show_cards()

# Translator
show_translator()

# Analytics Dashboard
show_analytics()

# Footer
show_footer()








