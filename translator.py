from deep_translator import GoogleTranslator

# Language codes
LANGUAGES = {
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


def translate_text(text, source_language, target_language):
    """
    Translate text using Google Translator.
    """

    source_code = LANGUAGES.get(source_language)
    target_code = LANGUAGES.get(target_language)

    if not source_code or not target_code:
        raise ValueError("Unsupported language selected.")

    translated = GoogleTranslator(
        source=source_code,
        target=target_code
    ).translate(text)

    return translated