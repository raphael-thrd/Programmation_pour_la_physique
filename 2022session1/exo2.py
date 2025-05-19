import numpy as np
import math

#=====on defini notre fonction serie de Taylor=============

def expmat(A, N=20):
    n = A.shape[0]
    result = np.eye(n, dtype=np.complex128) #fais une matrice identité n x n
    Ak = np.eye(n, dtype=np.complex128)#fais une matrice identité n x n
    for k in range(1, N + 1):
        Ak = Ak @ A
        coeff = 1.0 / math.factorial(k)
        result += coeff * Ak
    return result
    
    
#...Données du problème....
E1 = E2 = E3 = 1
eps2 = eps3 = 0.2
H = np.array([
    [E1, eps2, eps3],
    [eps2, E2, 0],
    [eps3, 0, E3]
], dtype=complex)

psi0 = np.array([1, 0, 0], dtype=complex)
t = 3
hbar = 1

#....évolution de l'état.....
A = -1j * H * t / hbar
ExpA = expmat(A, N=30)  # tu peux ajuster N si besoin
psi_t = ExpA @ psi0

print("psi(t) =", psi_t)

#ça sort un vecteur mais je n'ai pas vérifié

