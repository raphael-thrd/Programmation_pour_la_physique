#====Recherche de Zéro========

#..on definit notre fonction..
import numpy as np
def f(x):
	return np.sin(x)-1/x

	
#..on definit sa dérivée..
def df(x):
	return 1/x**2+np.cos(x)	



#..on utilise Newton....
def Newton(f,fprime, x0, epsilon=1e-9,maxit=400):
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
		

#..on fait une fonction qui trace f(x), pour trouver a peu pres les zeros...
def trace(f):
	import matplotlib.pyplot as plt
	x=np.linspace(0.5,10,100)
	y=[f(i) for i in x]
	plt.plot(x,y)
	plt.xlabel("x")
	plt.ylabel("f(x)")
	plt.grid()
	plt.axis("equal")
	plt.show()
	
#trace(f) #on voit qu'il y a des zeros vers 1.1,2.7,6.5,9.3

for n in [1, 2.1, 6, 9]:
	zero=Newton(f,df,n)




	
	
	
	
	
	
	
	
	
	
	
	
	
	
