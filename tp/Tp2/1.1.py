from support import *  # fonctions communes et imports du TP

def diviseurs(n):
    """Liste croissante des diviseurs positifs de n."""
    resultat = []
    for d in range(1, n + 1):
        if n % d == 0:
            resultat.append(d)
    return resultat

print(diviseurs(28))
print(diviseurs(97))