from support import *  # fonctions communes et imports du TP

def pgcd_naif(a, b):
    """PGCD par essai de tous les diviseurs possibles."""
    meilleur = 1
    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            meilleur = d
    return meilleur

def pgcd(a, b):
    """PGCD par l'algorithme d'Euclide."""
    while b != 0:
        a, b = b, a % b
    return a

print(pgcd_naif(1071, 462), pgcd(1071, 462))