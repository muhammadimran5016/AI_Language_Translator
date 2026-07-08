import pandas as pd
import os
from datetime import datetime

# CSV file to store translation history
HISTORY_FILE = "translation_history.csv"


def create_history_file():
    """
    Create the history CSV file if it doesn't exist.
    """

    if not os.path.exists(HISTORY_FILE):

        df = pd.DataFrame(
            columns=[
                "Date & Time",
                "Source Language",
                "Target Language",
                "Original Text",
                "Translated Text"
            ]
        )

        df.to_csv(HISTORY_FILE, index=False)


def save_translation(
    source_language,
    target_language,
    original_text,
    translated_text
):
    """
    Save one translation to history.
    """

    create_history_file()

    df = pd.read_csv(HISTORY_FILE)

    new_row = {
        "Date & Time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "Source Language": source_language,
        "Target Language": target_language,
        "Original Text": original_text,
        "Translated Text": translated_text,
    }

    df.loc[len(df)] = new_row

    df.to_csv(HISTORY_FILE, index=False)


def load_history():
    """
    Load all saved translations.
    """

    create_history_file()

    return pd.read_csv(HISTORY_FILE)


def clear_history():
    """
    Delete all translation history.
    """

    df = pd.DataFrame(
        columns=[
            "Date & Time",
            "Source Language",
            "Target Language",
            "Original Text",
            "Translated Text"
        ]
    )

    df.to_csv(HISTORY_FILE, index=False)