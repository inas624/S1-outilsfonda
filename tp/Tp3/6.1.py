from support import *  # fonctions communes et imports du TP

def somme(P, Q):
    """Somme de deux polynômes donnés par leurs coefficients."""
    longueur = max(len(P), len(Q))
    P = P + [0] * (longueur - len(P))
    Q = Q + [0] * (longueur - len(Q))
    return [P[i] + Q[i] for i in range(longueur)]

def produit_poly(P, Q):
    """Produit de deux polynômes donnés par leurs coefficients."""
    if not P or not Q:
        return []
    R = [0] * (len(P) + len(Q) - 1)
    for i in range(len(P)):
        for j in range(len(Q)):
            R[i + j] = R[i + j] + P[i] * Q[j]
    return R

print(somme([1, 2], [0, 0, 3]))
print(produit_poly([1, 1], [1, 1]))
print(produit_poly([-1, 1], [1, 1]))