from support import *  # fonctions communes et imports du TP

def evaluer_naif(P, x):
    """Évalue le polynôme P au point x, terme par terme."""
    total = 0
    for i in range(len(P)):
        total = total + P[i] * x ** i
    return total

print(evaluer_naif([2, 3, 0, 5], 2))
print(evaluer_naif([2, 3, 0, 5], 0))