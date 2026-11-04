from support import *  # fonctions communes et imports du TP

def transposee(A):
    """Transposée de la matrice A, donnée comme liste de lignes."""
    lignes = len(A)
    colonnes = len(A[0])
    return [[A[i][j] for i in range(lignes)] for j in range(colonnes)]

print(transposee([[1, 2, 3], [4, 5, 6]]))