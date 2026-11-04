from support import *  # fonctions communes et imports du TP

def arctangente_derivee(x):
    return 4 / (1 + x * x)

approx_trap = trapezes(arctangente_derivee, 0, 1, 1000)
approx_simp = simpson(arctangente_derivee, 0, 1, 1000)
print(approx_trap, abs(approx_trap - math.pi))
print(approx_simp, abs(approx_simp - math.pi))