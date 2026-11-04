from support import *  # fonctions communes et imports du TP

debut = time.perf_counter()
p = crible(100_000)
t_crible = time.perf_counter() - debut

debut = time.perf_counter()
combien = sum(1 for n in range(100_001) if est_premier(n))
t_un_par_un = time.perf_counter() - debut

print(len(p), combien)
print(f"crible {t_crible:.4f} s | un par un {t_un_par_un:.4f} s")