#=====Recherche de Zeros=======
#c'est une sorte de methode de la bisection

def zero(f,a,b,epsilon=1e-5):
	if f(a)*f(b) > 0:
		print("l'interval n'est pas bon")
		return
	c=(a*f(b)-b*f(a))/(f(b)-f(a))
	while abs(a-b)>=2*epsilon:
		c=(a*f(b)-b*f(a))/(f(b)-f(a))
		if f(a)*f(c)<0: #on verifie s'il y a un zéro entre a et c (ATTENTION il ne faut pas <=  !!(sinon ça converge pas)
			b=c
		else:
			a=c
	print("le zero est x=",c)
	return c
	
#...on definit la fonction...
import numpy as np
def f(x):
	return np.sin(x)+x-1
a=0
b=2	
zero=zero(f,a,b) # reponse, x=0.510973

#=========Graphe=======
import matplotlib.pyplot as plt

x=np.linspace(a,b,500)
y=[f(i) for i in x]

plt.plot(x,y,'r')
plt.plot(zero,0,'o',label=f"x={zero}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
