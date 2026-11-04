from support import *  # fonctions communes et imports du TP

def newton(P, depart, tolerance=1e-12, tours_max=100):
    """Racine du polynôme P par la méthode de Newton, à partir de depart."""
    derivee = deriver(P)
    x = float(depart)
    for tour in range(tours_max):
        valeur = evaluer(P, x)
        pente = evaluer(derivee, x)
        if pente == 0:
            raise ZeroDivisionError("tangente horizontale, Newton ne peut pas continuer")
        suivant = x - valeur / pente
        if abs(suivant - x) <= tolerance * max(1.0, abs(suivant)):
            return suivant, tour + 1
        x = suivant
    raise RuntimeError("pas de convergence en {} tours".format(tours_max))

# x^3 - 2x - 5
Q = [-5, -2, 0, 1]
racine, tours = newton(Q, 2)
print(racine, "en", tours, "tours")
print(abs(evaluer(Q, racine)) < 1e-10)