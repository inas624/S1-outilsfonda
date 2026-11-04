from support import *  # fonctions communes et imports du TP

for n in (20, 25, 30):
    print(f"F({n}) : {duree(fibonacci_recursif, n):.4f} s")