def validate_title(title):
    """Judul harus string, tidak kosong, maksimal 100 karakter."""
    if not isinstance(title, str):
        return False
    return 0 < len(title.strip()) <= 100


def clean_title(title):
    return title.strip()