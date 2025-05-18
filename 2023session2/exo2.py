import numpy as np
#====On definit nos fonctions

#..fonction de norme...
def norme(v):
	return np.sqrt(np.sum(v**2))
#..fonction de vecteur propre...

def vpropre(A,kmax=50):
	n=A.shape[0] #shape[0] donne le nombre de ligne de A
	v=np.zeros(n)
	v[0]=1
	v=v.reshape(n,1) #donne un vecteur colonne
	for i in range(kmax):
		v_ancien=v
		v=A@v_ancien/norme(A@v_ancien)
	
	Lambda=v.T@A@v
	
	return v,Lambda
	
#======recherche d'un vecteur propre===============

A=np.array([[1,-2,3],
	[-2,0,0.5],
	[3,0.5,2]])
v,Lambda=vpropre(A)

#====verification========

verif=A@v-Lambda*v

print(f"verification (bon si =0 ou proche) : A*v-Lambda*v={verif}")


