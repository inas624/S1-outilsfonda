from support import *  # fonctions communes et imports du TP

def deriver(P):
    """Coefficients du polynôme dérivé de P."""
    return [i * P[i] for i in range(1, len(P))]

print(deriver([2, 3, 0, 5]))
print(deriver([7]))