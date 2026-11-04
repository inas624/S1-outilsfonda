from support import *  # fonctions communes et imports du TP

for n in (10_007, 100_003, 1_000_003):
    t_naif = duree(est_premier_naif, n)
    t_rac = duree(est_premier, n)
    print(f"{n:>9} : naif {t_naif:.5f} s | racine {t_rac:.6f} s")