import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os

HISTORY_FILE = "translation_history.csv"


def show_analytics():
    """
    Display translation analytics dashboard.
    """

    if not os.path.exists(HISTORY_FILE):
        st.info("No translation history available.")
        return

    df = pd.read_csv(HISTORY_FILE)

    if df.empty:
        st.info("No translation history available.")
        return

    st.markdown("## 📊 Analytics Dashboard")

    # ---------------------------------
    # Statistics Cards
    # ---------------------------------

    total_translations = len(df)

    unique_source = df["Source Language"].nunique()
    unique_target = df["Target Language"].nunique()

    most_source = df["Source Language"].mode()[0]
    most_target = df["Target Language"].mode()[0]

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Total Translations", total_translations)
        st.metric("Source Languages Used", unique_source)

    with c2:
        st.metric("Most Used Source", most_source)
        st.metric("Most Used Target", most_target)

    st.markdown("---")

    # ---------------------------------
    # Source Language Bar Chart
    # ---------------------------------

    st.subheader("🌍 Source Language Usage")

    source_counts = df["Source Language"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(source_counts.index, source_counts.values)

    ax.set_xlabel("Language")
    ax.set_ylabel("Translations")
    ax.set_title("Source Language Usage")

    plt.xticks(rotation=45)

    st.pyplot(fig)