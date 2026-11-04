from support import *  # fonctions communes et imports du TP

Q = [-5, -2, 0, 1]
for depart in (2, 1, 0):
    racine, tours = newton(Q, depart)
    print(f"depart {depart:>2} : {tours:>2} tours, racine {racine:.9f}")