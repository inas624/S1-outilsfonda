from support import *  # fonctions communes et imports du TP

"""Fonctions communes utilisées dans plusieurs exercices du TP2."""
import math
import time
import random

def duree(fonction, *arguments):
    debut = time.perf_counter()
    fonction(*arguments)
    return time.perf_counter() - debut

def est_premier_naif(n):
    if n < 2: return False
    for d in range(2, n):
        if n % d == 0: return False
    return True

def est_premier(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0: return False
        d += 2
    return True

def crible(n):
    if n < 2: return []
    premier = [True] * (n + 1)
    premier[0] = premier[1] = False
    p = 2
    while p * p <= n:
        if premier[p]:
            for multiple in range(p * p, n + 1, p):
                premier[multiple] = False
        p += 1
    return [i for i, est_vrai in enumerate(premier) if est_vrai]

def fibonacci_recursif(n):
    if n < 0: raise ValueError("n doit être positif ou nul")
    if n < 2: return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)
