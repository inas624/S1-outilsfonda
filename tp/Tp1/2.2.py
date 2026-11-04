from support import *  # fonctions communes et imports du TP

def presque_egaux(a, b, tolerance=1e-9):
    """Dit si a et b sont égaux à la tolérance près."""
    return abs(a - b) <= tolerance

print(presque_egaux(0.1 + 0.2, 0.3))
print(presque_egaux(1.0, 1.5))