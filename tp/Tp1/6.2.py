from support import *  # fonctions communes et imports du TP

import sys

eps = 1.0
while 1.0 + eps / 2 != 1.0:
    eps = eps / 2

print(eps)
print(sys.float_info.epsilon)
print(eps == 2 ** -52)