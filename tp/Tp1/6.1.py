from support import *  # fonctions communes et imports du TP

def vers_binaire(n):
    """Écriture binaire de l'entier positif n, sans le préfixe 0b."""
    if n == 0:
        return "0"
    chiffres = ""
    while n > 0:
        chiffres = str(n % 2) + chiffres
        n = n // 2
    return chiffres

print(vers_binaire(37), vers_binaire(0), vers_binaire(1024))
print(all(vers_binaire(n) == bin(n)[2:] for n in range(2000)))