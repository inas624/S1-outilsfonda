from support import *  # fonctions communes et imports du TP

def racines(a, b, c):
    """Racines réelles de ax² + bx + c, sans élimination catastrophique."""
    delta = b * b - 4 * a * c
    if delta < 0:
        raise ValueError("pas de racine réelle")
    r = math.sqrt(delta)
    # on choisit le signe qui additionne au lieu de soustraire
    if b >= 0:
        sure = (-b - r) / (2 * a)
    else:
        sure = (-b + r) / (2 * a)
    autre = c / (a * sure)
    return min(sure, autre), max(sure, autre)

petite, grande = racines(1.0, -1e8, 1.0)
print(petite, grande)
print("produit :", petite * grande)
for x in (petite, grande):
    residu = x * x - 1e8 * x + 1
    print(f"residu : {residu:.1e}, soit {residu / max(x * x, 1.0):.1e} en relatif")