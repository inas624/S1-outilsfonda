from support import *  # fonctions communes et imports du TP

def newton_trace(P, depart, tours):
    """Renvoie la liste des premiers itérés de Newton, sans test d'arrêt."""
    derivee = deriver(P)
    x = float(depart)
    trajet = [x]
    for _ in range(tours):
        pente = evaluer(derivee, x)
        if pente == 0:
            break
        x = x - evaluer(P, x) / pente
        trajet.append(x)
    return trajet

R = [2, -2, 0, 1]          # x^3 - 2x + 2
print(newton_trace(R, 0, 8))

try:
    print(newton(R, 0))
except RuntimeError as erreur:
    print("echec :", erreur)