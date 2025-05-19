import numpy as np
import scipy as sc

#..Question....
#On sait que Qt=Q⁻¹ donc si on multiplie Rx=Qt*b par Q a gauche on a QRx=b et QR=A
#donc Ax=b


#....on definit des fonctions auxilliaires....

def norme(v): #norme d'un vecteur
	return np.sqrt(np.sum(v**2))

def projeter(v,w, epsilon=1e-10):
	vnorme=norme(v)
	if vnorme<epsilon: 
		return np.zeros(v.shape[0]) #projection sur un vecteur = vecteur nul
		
	resultat= np.copy(v)
	resultat *= v@w
	resultat /=vnorme**2
	return resultat


#....on va definir les algorithmes de gram schimdt et QR....

def gram_schmidt(A,epsilon=1e-10):
	n=A.shape[0]
	resultat=np.copy(A)
	for i in range(n):
		v=resultat[:,i] #pour tout vecteur de colone v
		vnorme=norme(v)
		if vnorme>=epsilon: #normaliser (sauf si nul)
			v/=vnorme
		for j in range(i+1,n): #pour toute colone apres v, 
			resultat[:,j]-= projeter(v,resultat[:,j],epsilon)#soustraire sa projection sur v
	return resultat
			
def decomp_QR(A, epsilon=1e-10):
	Q=gram_schmidt(A,epsilon)
	R=Q.T@A
	return Q,R
	
#======On resout maintenant l'equation=====================
#On sait que Rx=Qt*b, donc x=Inverse(R)*Qt*b

A=np.array([[1.5,4,2],
	[3,-2,0],
	[1,1,5]])
b=np.array([[7],[5],[-0.5]])

Q,R=decomp_QR(A)

x=np.linalg.inv(R)@Q.T@b

print(x)






			
			
			
			
			
