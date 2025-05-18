#====on défini la fonction de Laguerre=====
def L(n,x):
	if n==0:
		return 1
	elif n==1:
		return 1-x
	else:
		return ((2*n-1-x)*L(n-1,x)-(n-1)*L(n-2,x))/n #on utilise la recursivité pour appeler L dans L
		

#====graphique============
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,100) #on fait notre intervalle x€[0,5]
for k in range(1,4):

	n=[L(k,i) for i in x] #n est une liste ayant comme element les L avec n=k et x=la valeur de x a l'indice correspondant
	plt.plot(x,n,label=f"n={k}") #comme ca on plot directement dans la boucle

plt.xlabel("x")
plt.ylabel("L(x)") 

plt.legend()
plt.show()
