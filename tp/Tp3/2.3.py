from support import *  # fonctions communes et imports du TP

for degre in (200, 400, 800):
    P = [1] * (degre + 1)

    debut = time.perf_counter()
    a = evaluer_naif(P, 3)
    t_naif = time.perf_counter() - debut

    debut = time.perf_counter()
    b = evaluer(P, 3)
    t_horner = time.perf_counter() - debut

    print(f"degre {degre:>4} : rapport {t_naif / t_horner:.1f} | resultats egaux : {a == b}")