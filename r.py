import numpy as np
import sys

#returns the last position of a character c in an array of characters
def last_position(t,c):
    #we should work only on a prefix of the word uses in calcul_r
    n=len(t)
    #counter used to decrement
    i=n-1
    #last position of c, -1 by default
    k=-1
    while i>=0 and k==-1 :
        if t[i]==c:
            k=i
        i-=1
    return k



def calcul_r(u):
    n=len(u)
    #we initialize the r vector
    r=np.zeros(n,dtype=int)
    for i in range(0,n):
        #for each letter c of the word u, and a prefix u' s.t. u=u'cu''
        #we look at w, first suffic of u' starting with the letter c
        c=u[i]
        prefix=u[0:i]
        #start_of_w=last_position(prefix,c)
        start_of_w = prefix.rfind(c)

        if start_of_w==-1:
            r[i]=0
        else :
            r[i]=1+np.min(r[start_of_w:i])
    return r



def main():
    if len(sys.argv) !=2:
        return("usage: r.py [word]")
    else:
        word=sys.argv[1]
        return(calcul_r(word))

if __name__== "__main__":
    print(main())
    

