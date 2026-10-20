from config import Config


def validate_title(title):
    """Judul harus string, tidak kosong, maksimal sesuai konfigurasi."""
    if not isinstance(title, str):
        return False
    return 0 < len(title.strip()) <= Config.MAX_TITLE_LENGTH


def clean_title(title):
    return title.strip()
