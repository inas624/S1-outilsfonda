from support import *  # fonctions communes et imports du TP

def dichotomie(f, a, b, tolerance=1e-12):
    """Racine de f dans [a, b], par bissection. Exige f(a) et f(b) de signes opposés."""
    fa, fb = f(a), f(b)
    if fa == 0:
        return a
    if fb == 0:
        return b
    if fa * fb > 0:
        raise ValueError("f(a) et f(b) doivent etre de signes opposes")
    while b - a > tolerance:
        milieu = (a + b) / 2
        if f(a) * f(milieu) <= 0:
            b = milieu
        else:
            a = milieu
    return (a + b) / 2

def carre_moins_deux(x):
    return x * x - 2

racine = dichotomie(carre_moins_deux, 0, 2)
print(racine)
print(abs(racine - 2 ** 0.5) < 1e-9)