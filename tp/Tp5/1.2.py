from support import *  # fonctions communes et imports du TP

import unicodedata

def nettoyer(texte):
    """Majuscules sans accents, lettres A-Z uniquement."""
    sans_accent = unicodedata.normalize("NFD", texte)
    sans_accent = "".join(c for c in sans_accent if unicodedata.category(c) != "Mn")
    return "".join(c for c in sans_accent.upper() if "A" <= c <= "Z")

print(nettoyer("Été, à Paris !"))