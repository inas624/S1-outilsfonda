from support import *  # fonctions communes et imports du TP

def chiffrer(texte, a, b):
    """Chiffrement affine de texte avec la clé (a, b)."""
    resultat = []
    for c in nettoyer(texte):
        x = lettre_vers_nombre(c)
        resultat.append(nombre_vers_lettre((a * x + b) % 26))
    return "".join(resultat)

message = "ATTAQUEALAUBE"
print(chiffrer(message, 5, 8))
print(chiffrer(message, 1, 3))   # le chiffre de César