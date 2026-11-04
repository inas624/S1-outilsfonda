from support import *  # fonctions communes et imports du TP

def fibonacci(n):
    """F(n) par une boucle : deux variables suffisent."""
    precedent, courant = 0, 1
    for _ in range(n):
        precedent, courant = courant, precedent + courant
    return precedent

print(all(fibonacci(n) == fibonacci_recursif(n) for n in range(26)))
print(f"F(30) en {duree(fibonacci, 30):.6f} s")
grand = fibonacci(10_000)
print(len(str(grand)), "chiffres")