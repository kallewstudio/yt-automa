import re
import unicodedata

def sanitize_filename(filename):
    """
    Remove caracteres especiais, acentos e substitui espaços por "_".
    """
    # Remove acentos
    normalized = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode('ASCII')
    # Remove caracteres especiais
    sanitized = re.sub(r'[^A-Za-z0-9_\- ]+', '', normalized)
    # Substitui espaços por '_'
    return sanitized.replace(' ', '_')


