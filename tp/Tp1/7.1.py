from support import *  # fonctions communes et imports du TP

import math

def racines_naif(a, b, c):
    """Racines réelles de ax² + bx + c par la formule classique."""
    delta = b * b - 4 * a * c
    if delta < 0:
        raise ValueError("pas de racine réelle")
    r = math.sqrt(delta)
    return (-b - r) / (2 * a), (-b + r) / (2 * a)

petite, grande = racines_naif(1.0, -1e8, 1.0)
print(petite, grande)
print("produit :", petite * grande, "attendu : 1")