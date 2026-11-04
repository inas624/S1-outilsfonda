from support import *  # fonctions communes et imports du TP

appels = {}

def fibonacci_compte(n):
    appels[n] = appels.get(n, 0) + 1
    if n < 2:
        return n
    return fibonacci_compte(n - 1) + fibonacci_compte(n - 2)

resultat = fibonacci_compte(30)
print("F(30) =", resultat)
print("appels a F(1) :", appels[1])
print("appels en tout :", sum(appels.values()))