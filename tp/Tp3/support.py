from support import *  # fonctions communes et imports du TP

"""Imports et fonctions communes aux exercices du TP3."""
import math
import time

def evaluer_naif(P, x):
    return sum(P[i] * x ** i for i in range(len(P)))

def evaluer(P, x):
    total = 0
    for coefficient in reversed(P): total = total * x + coefficient
    return total

def deriver(P):
    return [i * P[i] for i in range(1, len(P))]

def newton(P, depart, tolerance=1e-12, tours_max=100):
    derivee = deriver(P)
    x = float(depart)
    for tour in range(tours_max):
        valeur, pente = evaluer(P, x), evaluer(derivee, x)
        if pente == 0: raise ZeroDivisionError("tangente horizontale")
        suivant = x - valeur / pente
        if abs(suivant - x) <= tolerance * max(1.0, abs(suivant)):
            return suivant, tour + 1
        x = suivant
    raise RuntimeError("pas de convergence en {} tours".format(tours_max))

def produit_poly(P, Q):
    if not P or not Q: return []
    R = [0] * (len(P) + len(Q) - 1)
    for i, a in enumerate(P):
        for j, b in enumerate(Q): R[i+j] += a*b
    return R

def rectangles(f, a, b, n):
    h=(b-a)/n
    return h*sum(f(a+i*h) for i in range(n))

def trapezes(f, a, b, n):
    h=(b-a)/n
    return h*((f(a)+f(b))/2+sum(f(a+i*h) for i in range(1,n)))

def simpson(f, a, b, n):
    if n % 2: n += 1
    h=(b-a)/n
    impairs=sum(f(a+i*h) for i in range(1,n,2))
    pairs=sum(f(a+i*h) for i in range(2,n,2))
    return h/3*(f(a)+f(b)+4*impairs+2*pairs)
