from support import *  # fonctions communes et imports du TP

import time

for degre in (1000, 5000, 20000):
    P = [1] * (degre + 1)

    debut = time.perf_counter()
    a = evaluer_naif(P, 1.0001)
    t_naif = time.perf_counter() - debut

    debut = time.perf_counter()
    b = evaluer(P, 1.0001)
    t_horner = time.perf_counter() - debut

    print(f"degre {degre:>6} : naif {t_naif:.5f} s | horner {t_horner:.5f} s "
          f"| rapport {t_naif / t_horner:.1f} | ecart des valeurs {abs(a - b):.2e}")