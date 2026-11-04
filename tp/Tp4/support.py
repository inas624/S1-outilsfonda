from support import *  # fonctions communes et imports du TP

"""Imports et fonctions communes aux exercices du TP4."""
import math
import random
import time
try:
    import numpy as np
except ImportError:
    np = None

def matrice_aleatoire(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

def rotation(angle):
    if np is None: raise ImportError("Installez NumPy avec : pip install numpy")
    c, s = math.cos(angle), math.sin(angle)
    return np.array([[c, -s], [s, c]])

def angle(u, v):
    produit = u[0]*v[0] + u[1]*v[1]
    nu = math.hypot(u[0],u[1]); nv = math.hypot(v[0],v[1])
    if nu == 0 or nv == 0: raise ValueError("un vecteur nul n'a pas d'angle")
    return math.acos(max(-1.0,min(1.0,produit/(nu*nv))))

def resoudre(A, b, tolerance=1e-14):
    n=len(A)
    if n == 0 or len(b) != n or any(len(ligne) != n for ligne in A):
        raise ValueError("dimensions incompatibles")
    M=[list(A[i])+[b[i]] for i in range(n)]
    for k in range(n):
        pivot=max(range(k,n), key=lambda i: abs(M[i][k]))
        if abs(M[pivot][k]) <= tolerance: raise ValueError("systeme singulier ou mal pose")
        M[k],M[pivot]=M[pivot],M[k]
        for i in range(k+1,n):
            facteur=M[i][k]/M[k][k]
            for j in range(k,n+1): M[i][j]-=facteur*M[k][j]
    x=[0]*n
    for i in range(n-1,-1,-1):
        x[i]=(M[i][n]-sum(M[i][j]*x[j] for j in range(i+1,n)))/M[i][i]
    return x

def produit(A, B):
    """Produit matriciel A x B, pour des matrices sous forme de listes."""
    n, p = len(A), len(A[0])
    if len(B) != p:
        raise ValueError("dimensions incompatibles")
    q = len(B[0])
    C = [[0] * q for _ in range(n)]
    for i in range(n):
        for j in range(q):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(p))
    return C
