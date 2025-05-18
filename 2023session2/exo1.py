#====On defint la fonciton sigma==================
def sigma(n):
	x=n #un nombre est un diviseur de lui même
	for i in range(1,n):
		if n%i==0: #si le reste de la division entre n et i est 0
			x+=i #on ajoute i à x
	return x
			
#========on trace la fonction======================

import matplotlib.pyplot as plt
N=100
X=[i for i in range(1,N)]
Y=[sigma(i) for i in range(1,N)]

plt.plot(X,Y)
plt.xlabel("n")
plt.ylabel("sigma(n)")

plt.show()
