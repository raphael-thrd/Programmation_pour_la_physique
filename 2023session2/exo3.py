#====Definition des algorithmes===========
#on va utiliser Levenberg-Marquard

def lev_mar(t, u, y, f, gradf, beta0, lam0=1e-4, epsilon=1e-2):
    beta = np.copy(beta0)  # paramètres à ajuster
    delta = np.ones(len(beta))  # différence entre deux itérations
    lam = lam0
    p = len(beta)
    
    r = f(t, u, beta) - y
    chi2 = np.sum(r**2)

    while True:
        # Calcul de la matrice Jacobienne avec les dérivées partielles
        J = np.array([df(t, u, beta) for df in gradf]).T
        M = J.T @ J + lam * np.identity(p)

        delta = gauss(M, -r @ J)  # méthode de Gauss-Newton modifiée
        rnew = f(t, u, beta + delta) - y  # nouveau résidu
        chi2new = np.sum(rnew**2)  # nouveau chi2

        if chi2new > chi2:
            lam *= 10
        else:
            beta += delta
            if chi2 - chi2new < epsilon:
                break
            r = rnew
            chi2 = chi2new
            lam /= 10

    return beta, chi2

#on definit la fonction gauss pour resolution lineaire(on peut prendre celui du cours aussi)
def gauss(A, b):
    return np.linalg.solve(A, b)

#on defini la fonction Y

def f(T,P, beta):
	return beta[0]+beta[1]*T+beta[2]*P


#on definit les fonctions derivées par rapport aux parametres

gradf = [
    lambda T, P, beta: np.ones_like(T),  # ∂f/∂β₀
    lambda T, P, beta: T,                # ∂f/∂β₁
    lambda T, P, beta: P                 # ∂f/∂β₂
]
	
#======recuperation des donnees=====================
import numpy as np

data=np.loadtxt("rendement.txt").T #on prend la transposé pour que data[0] soit Y et pas data[:,0]
Y=data[0]
T=data[1]
P=data[2]

#..conditions initiales...
beta0 = np.array([10., 5.0, 10.0])


beta_opt, chi2=lev_mar(T,P,Y,f,gradf,beta0)

print(beta_opt, chi2)






