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



def calcul_r(s):
    n=len(s)
    r=np.zeros(n,dtype=int)
    for i in range(0,n):
        c=s[i]
        prefix=s[0:i]
        start_ofsubword=last_position(prefix,c)
        if start_ofsubword==-1:
            r[i]=0
        else :
            r[i]=1+np.min(r[start_ofsubword:i])
    return r

def main():
    if len(sys.argv) !=2:
        print("usage: r.py [word]")
    else:
        word=sys.argv[1]
        print(calcul_r(word))

if __name__== "__main__":
    main()
    

