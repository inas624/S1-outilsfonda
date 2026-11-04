from support import *  # fonctions communes et imports du TP

def euclide_etendu(a, b):
    """Renvoie (g, u, v) avec g = pgcd(a, b) et a u + b v = g."""
    if b == 0:
        return a, 1, 0
    g, u, v = euclide_etendu(b, a % b)
    return g, v, u - (a // b) * v

g, u, v = euclide_etendu(1071, 462)
print(g, u, v, 1071 * u + 462 * v == g)