from support import *  # fonctions communes et imports du TP

def rectangles(f, a, b, n):
    """Intégrale de f sur [a, b] par n rectangles à gauche."""
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))

def trapezes(f, a, b, n):
    """Intégrale de f sur [a, b] par n trapèzes."""
    h = (b - a) / n
    interieur = sum(f(a + i * h) for i in range(1, n))
    return h * ((f(a) + f(b)) / 2 + interieur)

def simpson(f, a, b, n):
    """Intégrale de f sur [a, b] par la méthode de Simpson, n pair."""
    if n % 2 == 1:
        n = n + 1
    h = (b - a) / n
    impairs = sum(f(a + i * h) for i in range(1, n, 2))
    pairs = sum(f(a + i * h) for i in range(2, n, 2))
    return h / 3 * (f(a) + f(b) + 4 * impairs + 2 * pairs)

def carre(x):
    return x * x

for n in (10, 100, 1000):
    e_rect = abs(rectangles(carre, 0, 1, n) - 1 / 3)
    e_trap = abs(trapezes(carre, 0, 1, n) - 1 / 3)
    e_simp = abs(simpson(carre, 0, 1, n) - 1 / 3)
    print(f"n = {n:>4} : rectangles {e_rect:.1e} | trapezes {e_trap:.1e} | simpson {e_simp:.1e}")