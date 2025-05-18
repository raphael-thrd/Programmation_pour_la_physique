#===Commentaire======
"""
1. epsilon est tres proche de 0, dans le pire des cas f(x)=0 pour 1-epsilon<x<1, donc 1-epsilon =x*epsilon si epsilon =1e-n alors il y a au maximum 10^n - 1 itération à faire (pas sûr d'avoir bien compris la question)

cette méthode à l'avantage d'être facile à comprendre et à implémenter, mais elle est lente. ce n'est pas une bonne alternative car les problèmes physique sont plus complexe, et demanderai donc enormement de temps pour à cet algorithme

"""

#====implémentation de l'algorithme========
import numpy as np
def f(x):
	return x*np.sin(x)-1/2
	
def fzero(f,epsilon=1e-5, imax=1e8): #fonction qui cherche les zéros
	x=epsilon
	k=2
	i=0
	while f(x)<0:
		x=k*epsilon
		i+=1
		k+=1
		if i>imax:
			print("ne converge pas")
			return
	print(f"le zero est à x={x}")
	return x 
	
fzero(f)
#je trouve la bonne valeur


#======recherche de zéro avec Newton========

#...on fait la fonction dérivé....

def df(x):
	return x*np.cos(x)+np.sin(x)
	
#..on implémente Newton...

def Newton(f,fprime, x0, epsilon=1e-11,maxit=400):
	i=0 #sert pour maxit
	x=x0
	x_ancien=x0+2*epsilon
	
	while abs(x-x_ancien)>epsilon:
		if fprime(x)==0:
			print("division par zéro, arret du programme")
			return

		x_ancien=x
		x=x-f(x)/fprime(x)
		i+=1
		if i>maxit:
			print("pas de convergence")
			return
	print(f"Zeros trouve à x={x:.9f}")
	return x
	
Newton(f,df,0.7)

#pour Newton il faut etre proche du Zéro, il faut le connaitre avant, contrairement a l'autre technique







