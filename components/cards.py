import streamlit as st


def show_cards():
    """Display information and statistics cards."""

    # ---------- Custom CSS ----------
    st.markdown("""
    <style>

    .info-card{
        background:#F4F8FF;
        border-left:6px solid #2563EB;
        padding:22px;
        border-radius:15px;
        margin-top:10px;
        margin-bottom:25px;
    }

    .info-title{
        font-size:26px;
        font-weight:bold;
        color:#2563EB;
        margin-bottom:15px;
    }

    .info-text{
        font-size:18px;
        line-height:2;
    }

    .stat-card{
        background:white;
        border-radius:15px;
        padding:22px;
        text-align:center;
        box-shadow:0px 4px 12px rgba(0,0,0,0.10);
    }

    .stat-number{
        font-size:34px;
        font-weight:bold;
        color:#2563EB;
    }

    .stat-title{
        font-size:18px;
        color:#555;
        margin-top:10px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------- How to Use ----------
    st.markdown("""
    <div class="info-card">

    <div class="info-title">
    💡 How to Use
    </div>

    <div class="info-text">
    1️⃣ Select Source Language<br>
    2️⃣ Select Target Language<br>
    3️⃣ Enter your text<br>
    4️⃣ Click Translate<br>
    5️⃣ Listen, Download or View History
    </div>

    </div>
    """, unsafe_allow_html=True)

    # ---------- Statistics ----------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">20+</div>
            <div class="stat-title">Languages</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">AI</div>
            <div class="stat-title">Powered</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">1.0</div>
            <div class="stat-title">Version</div>
        </div>
        """, unsafe_allow_html=True)


