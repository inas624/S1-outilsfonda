from support import *  # fonctions communes et imports du TP

def facteurs(n):
    """Facteurs premiers de n, avec multiplicité, dans l'ordre croissant."""
    resultat = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            resultat.append(d)
            n = n // d
        d = d + 1
    if n > 1:
        resultat.append(n)
    return resultat

f = facteurs(360)
print(f)

produit = 1
for x in f:
    produit = produit * x
print(produit)