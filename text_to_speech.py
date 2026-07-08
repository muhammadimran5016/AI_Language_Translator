from gtts import gTTS
import tempfile
import os

# Language codes supported by gTTS
TTS_LANGUAGES = {
    "English": "en",
    "Urdu": "ur",
    "Arabic": "ar",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Turkish": "tr",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Malay": "ms",
    "Thai": "th",
    "Dutch": "nl",
    "Greek": "el",
}


def generate_speech(text, language):
    """
    Convert translated text into speech and
    return the path of the generated mp3 file.
    """

    language_code = TTS_LANGUAGES.get(language, "en")

    tts = gTTS(
        text=text,
        lang=language_code,
        slow=False
    )

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    tts.save(temp_file.name)

    return temp_file.name