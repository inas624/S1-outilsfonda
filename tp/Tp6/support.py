from support import *  # fonctions communes et imports du TP

"""Fonctions et imports communs aux exercices du TP6."""
import math

def vecteur(A,B): return (B[0]-A[0],B[1]-A[1])
def produit_scalaire(u,v): return u[0]*v[0]+u[1]*v[1]
def norme(u): return math.hypot(u[0],u[1])
def determinant(u,v): return u[0]*v[1]-u[1]*v[0]
def orientation(A,B,C):
    d=determinant(vecteur(A,B),vecteur(A,C))
    return 1 if d>0 else (-1 if d<0 else 0)
def aire(polygone):
    if len(polygone)<3: return 0
    s=0
    for i,(x1,y1) in enumerate(polygone):
        x2,y2=polygone[(i+1)%len(polygone)]
        s += x1*y2-x2*y1
    return abs(s)/2
def dedans(P,polygone):
    x,y=P; interieur=False
    for i,(x1,y1) in enumerate(polygone):
        x2,y2=polygone[(i+1)%len(polygone)]
        if (y1>y)!=(y2>y):
            xc=x1+(y-y1)*(x2-x1)/(y2-y1)
            if x<xc: interieur=not interieur
    return interieur
def tracer_polygone(polygone, points=None):
    # Le tracé est enregistré dans un PNG pour ne pas bloquer l'exécution du TP.
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        xs=[p[0] for p in polygone]+[polygone[0][0]]
        ys=[p[1] for p in polygone]+[polygone[0][1]]
        plt.figure(); plt.plot(xs,ys,marker="o")
        if points:
            plt.scatter([p[0] for p in points],[p[1] for p in points])
        plt.axis("equal"); plt.grid(True); plt.savefig("etoile_tp6.png"); plt.close()
        print("Tracé enregistré dans etoile_tp6.png")
    except ImportError:
        print("Matplotlib absent : tracé non généré (pip install matplotlib)")

# Polygone commun repris dans plusieurs exercices.
maison = [(0, 0), (2, 0), (2, 1.5), (1, 2.5), (0, 1.5)]
