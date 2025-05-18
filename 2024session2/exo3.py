import numpy as np
#====On defini la'algorithme==========
def resoudre_relax(A,b,omega,kmax=100):
	x=np.copy(b)
	w=omega
	for i in range(kmax):
		x_ancien=x
		x=x_ancien-omega*(A@x_ancien-b)
	return x
	
#====On teste=====
A=np.array([[3,1,-1],
	[2,2,1],
	[0.5,-0.5,3]])
b=np.array([1,0,0]).T
omega=0.1
x=resoudre_relax(A,b,omega)

print(x)
#on trouve la bonne valeur [ 0.40625 -0.34375 -0.125  ]

