from support import *  # fonctions communes et imports du TP

binome = [1]
for _ in range(10):
    binome = produit_poly(binome, [1, 1])
print(binome)
print(sum(binome), 2 ** 10)