#==definition de la fonction=====

def doublefac(n):
	if n<=0:
		return 1
	else:
		return n*doublefac(n-2) #on fait une recursion sur le n-2 pour garder la parité
		

#=====graphe======
import numpy as np
import matplotlib.pyplot as plt


x=[i for i in range(21)] #mets dans une liste [0,1,2,..,20]
y=[np.log(doublefac(n)) for n in x] #mets dans une liste [ln(0!!),ln(1!!),ln(2!!),...]

plt.plot(x,y, "o")
plt.xlabel("x")
plt.ylabel("ln(x!!)")
plt.show()
