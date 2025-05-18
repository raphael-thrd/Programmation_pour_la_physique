#====on défini la fonction J0============
import scipy.special

def J0(x,N=20):
	J=0 #variable dynamique
	for k in range(N+1):
		J+=(-1)**k/scipy.special.factorial(k)**2*(x/2)**(2*k)
	return J

#=====on trace le graphique de notre fonction==========

import matplotlib.pyplot as plt 
import numpy as np

N=11

X=[i for i in range(N)] #fait une liste avec les elements de la boucle
Y=np.zeros(N)
Y_scipy=np.zeros(N)

for i in range(N):
	Y[i]=J0(i)
	Y_scipy[i]=scipy.special.j0(i)

plt.plot(X,Y,label="J0")
plt.plot(X,Y_scipy,label="J0 scipy")

plt.legend()
plt.show()


#======recherche des Zeros============================================

#on utilise la methode de Newton

#fonction de derivation
def d(f,epsilon=10e-5):
    
	def g(x):
		return (f(x+epsilon)-f(x-epsilon))/(2*epsilon)
	return g
	
dJ0=d(J0)

#....Newton.....

def Newton(f,fprime, x0, epsilon=1e-3,maxit=200):
	i=0 #sert pour maxit
	x=x0
	x_ancien=x0+2*epsilon
	
	while abs(x-x_ancien)>epsilon:
		if fprime(x)==0:
			print("division par zéro, arret du programme")
			return
		x_ancien=x
		x=x-f(x)/fprime(x)
		
		if i>maxit:
			print("pas de convergence")
			return
		print(f"Zeros trouve à x={x:.3f}")
	return x
		

#..maintenant on cherche les zeros par itération....

for n in [3,5,8]: #on a vu sur notre graphique que les premiers zeros sont vers 2, 5, 8
	zero=Newton(J0,dJ0,n)

	















