import numpy as np

def f(x):
	return x**2 -2*np.cos(x+1)


#...On cherche la position approximative des zéros (necessaire pour Newton)...
x=np.linspace(-2,2,500)
y=[f(t) for t in x]

import matplotlib.pyplot as plt

plt.plot(x,y)
plt.title("on regarde où sont les zéros à peu près")
plt.grid()
plt.show() #on voit qu'il y a des zeros en -1.4 et 0.4


#======Recherche de Zero==========
def fprime(x):
	return 2*x+2*np.sin(x+1)




#....Newton...

def Newton(f,fprime, x0, epsilon=1e-8,maxit=200):
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
	print(f"Zeros trouve à x={x:.8f}")
	return x

for n in [-1.4, 0.4]:
	zero=Newton(f,fprime,n)
	plt.plot(zero,0, "o",label=f"x={zero}")#..On affiche les zeros sur le graphe...
plt.plot(x,y)
plt.legend()
plt.show()



