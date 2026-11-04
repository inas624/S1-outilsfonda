from support import *  # fonctions communes et imports du TP

n = 2026
d = 7
quotient = n // d
reste = n % d
print(quotient, reste)
print(quotient * d + reste == n)