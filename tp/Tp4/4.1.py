from support import *  # fonctions communes et imports du TP

def resoudre(A, b, tolerance=1e-14):
    """Résout A x = b par le pivot de Gauss avec pivot partiel.

    A est une liste de lignes, b une liste. Ni A ni b ne sont modifiés.
    Un pivot inférieur ou égal à tolerance est considéré comme nul.
    """
    n = len(A)
    # copie de travail, matrice augmentée [A | b]
    M = [list(A[i]) + [b[i]] for i in range(n)]

    for k in range(n):
        # pivot partiel : la ligne dont le coefficient est le plus grand en valeur absolue
        meilleure = max(range(k, n), key=lambda i: abs(M[i][k]))
        if abs(M[meilleure][k]) <= tolerance:
            raise ValueError("systeme singulier ou mal pose")
        M[k], M[meilleure] = M[meilleure], M[k]

        # élimination sous la diagonale
        for i in range(k + 1, n):
            facteur = M[i][k] / M[k][k]
            for j in range(k, n + 1):
                M[i][j] = M[i][j] - facteur * M[k][j]

    # remontée : on résout de la dernière équation vers la première
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        somme = M[i][n]
        for j in range(i + 1, n):
            somme = somme - M[i][j] * x[j]
        x[i] = somme / M[i][i]
    return x

A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
b = [2, -1, 8]
x = resoudre(A, b)
print([round(v, 10) for v in x])


verif = [sum(A[i][j] * x[j] for j in range(3)) for i in range(3)]
print([round(v, 10) for v in verif])