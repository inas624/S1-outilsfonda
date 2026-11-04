from support import *  # fonctions communes et imports du TP

import math

def heron(a, tolerance=1e-12):
    """Racine carrée de a par la méthode de Héron."""
    if a < 0:
        raise ValueError("pas de racine carrée réelle pour un nombre négatif")
    if a == 0:
        return 0.0
    x = float(a)
    tours = 0
    while True:
        suivant = 0.5 * (x + a / x)
        tours = tours + 1
        if abs(suivant - x) <= tolerance * abs(suivant):
            return suivant
        x = suivant

print(heron(2))
print(math.sqrt(2))
print(abs(heron(2) - math.sqrt(2)) < 1e-12)