import numpy as np
import sys
from r import calcul_r 
from l import calcul_l 


def calcul_m(u):
    r = calcul_r(u)
    l = calcul_l(u)
    s = r+l
    return(1+np.max(s))

def main():
    if len(sys.argv) !=2:
        return("usage: r.py [word]")
    else:
        word=sys.argv[1]
        return(calcul_m(word))

if __name__== "__main__":
    print(main())
    

