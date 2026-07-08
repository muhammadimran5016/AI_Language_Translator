import os
import streamlit as st

from translator import translate_text, LANGUAGES
from text_to_speech import generate_speech
from history import save_translation, load_history


def show_translator():
    """Translator User Interface"""

    st.markdown("## 🌐 Translation")

    languages = list(LANGUAGES.keys())

    # -----------------------------
    # Language Selection
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        source_language = st.selectbox(
            "🌍 Source Language",
            languages,
            index=0,
        )

    with col2:
        target_language = st.selectbox(
            "🎯 Target Language",
            languages,
            index=1,
        )

    # -----------------------------
    # Input
    # -----------------------------
    st.markdown("### 📝 Enter Text")

    input_text = st.text_area(
        "",
        height=180,
        placeholder="Type or paste your text here..."
    )

    # -----------------------------
    # Translate
    # -----------------------------
    if st.button("🚀 Translate", use_container_width=True):

        if input_text.strip() == "":
            st.warning("Please enter some text.")
            return

        if source_language == target_language:
            st.warning("Source and Target languages cannot be the same.")
            return

        with st.spinner("Translating..."):

            try:

                translated_text = translate_text(
                    input_text,
                    source_language,
                    target_language
                )

                st.session_state["translated_text"] = translated_text

                # Save translation history
                save_translation(
                    source_language,
                    target_language,
                    input_text,
                    translated_text
                )

                st.success("Translation saved successfully!")

            except Exception as e:
                st.error(f"Translation Error: {e}")

    st.markdown("---")

    # -----------------------------
    # Output
    # -----------------------------
    st.markdown("### 🌍 Translated Text")

    translated_text = st.session_state.get("translated_text", "")

    st.text_area(
        "",
        value=translated_text,
        height=180,
        disabled=True,
    )

    st.markdown("")

    # -----------------------------
    # Action Buttons
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("📋 Copy", use_container_width=True):

            if translated_text:
                st.success(
                    "Copy feature will be connected later."
                )
            else:
                st.warning("Nothing to copy.")

    with col2:

        st.download_button(
            label="📥 Download",
            data=translated_text,
            file_name="translated_text.txt",
            mime="text/plain",
            use_container_width=True,
            disabled=(translated_text == "")
        )

    with col3:

        if st.button(
            "🔊 Speak",
            use_container_width=True,
            disabled=(translated_text == "")
        ):

            try:

                audio_file = generate_speech(
                    translated_text,
                    target_language
                )

                with open(audio_file, "rb") as audio:
                    st.audio(audio.read(), format="audio/mp3")

                if os.path.exists(audio_file):
                    os.remove(audio_file)

            except Exception as e:
                st.error(f"Speech Error: {e}")

    # -----------------------------
    # Translation History
    # -----------------------------
    st.markdown("---")
    st.markdown("## 📜 Translation History")

    history_df = load_history()

    if history_df.empty:
        st.info("No translation history available.")
    else:
        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )