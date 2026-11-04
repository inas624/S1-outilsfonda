from support import *  # fonctions communes et imports du TP

def nombre_de_chiffres(n):
    """Renvoie le nombre de chiffres de l'entier positif n."""
    compte = 1
    while n >= 10:
        n = n // 10
        compte = compte + 1
    return compte

print(nombre_de_chiffres(2026))
print(nombre_de_chiffres(7))
print(nombre_de_chiffres(10 ** 60))