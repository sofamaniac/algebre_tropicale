import numpy as np
import sys
from r import last_position


def calcul_matrix(u):
	n = len(u)
	#on initialise toutes les cases de M à l'infini
	M = np.full((n,n),np.Inf)
	un = np.full(n,1)
	for i in range(n):
		#lp pour last_position
		#A noter que on a forcément lp>=0
		u2 = u+u[:i]
		lp = last_position(u2,u[i]) 
		#il faut initialiser la première ligne
		if i == 0:
			M[i,lp:n]=1
		else : 
			#il faut s'assurer, pour ne pas calculer le minimum d'une matrice vide, que le sous mot que l'on regarde n'est pas un facteur de u 
			
			if (max(0,lp-n))<=i :
				M[i] = np.amin(M[max(0,lp-n) :i],0) + un
			M[i,lp:n]=1
			
				
	return M
					
			
		
				
		


def main():
    if len(sys.argv) !=2:
        return("usage: r.py [word]")
    else:
        word=sys.argv[1]
        return(calcul_matrix(word))

if __name__== "__main__":
    print(main())
    

