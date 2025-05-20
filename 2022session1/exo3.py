#====Definition de notre fonction=============
import numpy as np

def f(t,beta):
	return beta[0] + beta[1]*t+beta[2]*np.sin(2*np.pi * t)	
	
#...Et de ses dérivées par rapport aux paramêtres......

gradf= [lambda t, beta: [1]*len(t),
	lambda t, beta: t,
	lambda t, beta: np.sin(2*np.pi*t)]


"""
#===Definition de Triangulariser pour Gauss==============
def triangulariser( M ) :
	n = M.shape[0] # le nombre de lignes
	for i in range( n ) : # boucle sur les premi `e res n colonnes
		for k in range(i , n ) : # chercher pivot sous la diagonale
			if M[k , i ] != 0: # pivot trouv ´e dans ligne k ?
				M[[ i , k ] , :] = M[[ k , i ] , :] # ´e changer lignes i et k
				pivot = M[i , i ] # m ´e moriser pivot
				break # quitter boucle sur k
			else : # tous les ´e l ´e ments sous la diagonale sont z ´e ro ?
				continue # alors rien `a faire pour cette colonne
			for k in range ( i +1 , n ) : # éliminer tout sous la diag .:
				facteur = -M[k , i ]/ pivot # ajouter ( facteur ) ...
				M[k , :] += facteur * M[i , :] # ...*( ligne du pivot )
                                                # `a la ligne k .

#=====definition de Gauss pour Levenberg-Marquardt=============================

def gauss(A , b ) : # trouver la solution x de Ax = b
    n = A . shape[0] # le nombre de lignes
    M = np . empty(( n , n +1) ) # la matrice M
    M[: , : n ] = np . copy( A ) # copier A dans les 1 `e res n colonnes
    M[: , n ] = np . copy ( b ) # copier b dans la derni `e re colonne
    triangulariser( M ) # apr `es , M est triangulaire sup ´e rieure

    x = np.empty( n ) # on mettra la solution ici
    for i in range(n -1 , -1 , -1) : # parcourir lignes en arri `e re
        sigma = 0. # la somme des x que l ’ on conna ^ı t d ´e j `a
        for k in range( i +1 , n ) : # ... * les M_ik correspondants
            sigma += M[i , k ] * x[ k ]
        if M[i , i ] == 0: # Matrice singulière ?
            if M[i , n ] - sigma == 0: # faut r ´e soudre 0* x [ i ] = 0 ?
                print ( " Attention , solution pas unique ! " )
                x[ i ] = 42
            else : # faut résoudre 0* x [ i ] = ( non nul ) ?
                print ( " Erreur , pas de solution " )
                return
        else : # sinon on peut diviser par M [i , i ]
            x[ i ] = ( M[i , n ] - sigma ) / M[i , i ]
    return x

"""
#====on peut aussi faire========
def gauss(A, b):
    return np.linalg.solve(A, b)

#====Définition de Levenberg-Marquardt============

def lev_mar(t , y , f , gradf , beta0 ,lam0=1.E-4, epsilon =1.E-5) :
    beta = np.copy( beta0 ) # les paramètres à ajuster
    delta = np.ones( len( beta ) ) # diff . entre deux itérations
    lam=lam0
    p=len(beta)
    r=f(t,beta)-y
    chi2=np.sum(r**2)

    while True:
        J = np.array([ df(t , beta ) for df in gradf ]).T # matr . J
        M=J.T @ J +lam*np.identity(p)
        delta = gauss(M, -r@J) #Gauss Newton modifié
        rnew= f(t,beta+delta)-y #nouveau résidu
        chi2new=np.sum(rnew**2) #nouveau X²

        if chi2new > chi2:
            lam= lam*10
        else:
            beta +=delta
            if chi2-chi2new < epsilon:
                break
            r=rnew
            chi2=chi2new
            lam= lam/10

    return beta , chi2
    
#====regression==========

#...extraction des données...
data=np.loadtxt("data.txt").T 

t=data[0]
y=data[1]

beta0 =[1.,0.5,1.] #je ne sais pas comment choisir les parametres initiaux 

beta, chi2=lev_mar(t,y,f,gradf,beta0)

#========On affiche le graphe========
import matplotlib.pyplot as plt

x=np.linspace(0,3,100)
y_ajust=[f(k,beta) for k in x]

plt.plot(x,y_ajust, label="regression Lev-Mar")
plt.plot(t,y, label="donnees experimentales")
plt.xlabel("t")
plt.ylabel("y")
plt.title(f"y={beta[0]:.3f} + {beta[1]:.3f}*t + {beta[2]:.3f}*sin(2pi*t)")
plt.legend()
plt.show()

 


 
    
    
    
    
    
    
   
   
   
   
   
   
   
   
   
   
   
