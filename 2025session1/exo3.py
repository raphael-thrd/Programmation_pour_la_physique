#...Commentaire.........
#on sait que A=LL^T
#On va utiliser la Decomposition LU: PA=LU 
#avec L=L U=L^T et P=Identité


import numpy as np
import scipy.linalg as la

# Fonction du cours decomposition LU : resout LUx = Pb

def resoudre(L, U, P, b):
    n = U.shape[0]
    bprime = P @ b
    y = np.zeros(n)
    for i in range(n):
        sigma = sum(L[i, k] * y[k] for k in range(i))
        y[i] = (bprime[i] - sigma) / L[i, i]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        sigma = sum(U[i, k] * x[k] for k in range(i+1, n))
        x[i] = (y[i] - sigma) / U[i, i]
    return x

A = np.array([[3, 2, 1],
              [2, 4, 0],
              [1, 0, 6]])

b = np.array([-1, 1, 0])

# Décomposition de Cholesky : A = LL^T
L = la.cholesky(A, lower=True)
U = L.T
P = np.identity(3)  # identité car pas de permutation

x = resoudre(L, U, P, b)

# Affichage de la solution
print(f"Solution x ={x}")
