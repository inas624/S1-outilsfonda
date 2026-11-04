from support import *  # fonctions communes et imports du TP

random.seed(7)
n = 50
A = matrice_aleatoire(n)
b = [random.random() for _ in range(n)]

mienne = resoudre(A, b)
celle_de_numpy = np.linalg.solve(np.array(A), np.array(b))

ecart = max(abs(mienne[i] - celle_de_numpy[i]) for i in range(n))
print("ecart maximal :", ecart)
print(ecart < 1e-9)