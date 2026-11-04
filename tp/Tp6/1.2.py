from support import *  # fonctions communes et imports du TP

def determinant(u, v):
    """Déterminant de (u, v), aire orientée du parallélogramme qu'ils engendrent."""
    return u[0] * v[1] - u[1] * v[0]

def distance_point_droite(P, A, B):
    AB = vecteur(A, B)
    AP = vecteur(A, P)
    return abs(determinant(AB, AP)) / norme(AB)

print(distance_point_droite((0, 0), (0, 1), (1, 0)), math.sqrt(2) / 2)
print(distance_point_droite((3, 4), (0, 0), (1, 0)))