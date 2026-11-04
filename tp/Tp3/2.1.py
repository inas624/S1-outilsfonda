from support import *  # fonctions communes et imports du TP

def evaluer(P, x):
    """Évalue le polynôme P au point x par le schéma de Horner."""
    total = 0
    for coefficient in reversed(P):
        total = total * x + coefficient
    return total

P = [2, 3, 0, 5]
for x in (-2, 0, 1, 2, 10):
    print(x, evaluer_naif(P, x), evaluer(P, x))