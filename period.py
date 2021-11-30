import numpy as np
import sys
from r import calcul_r
import re


def d_vector(r):
    """Return the vector of substractions of 2 consecutive elements in r"""
    d = []
    for i in range(len(r) - 1):
        d.append(r[i+1]-r[i])
    return d


def z_algo(d):
    """ Return (maybe ?) the period of the input vector
        Compute the array z such that z[i] contains the length of the
        longest prefix of d'[i..n] that is also a prefix of d'[1..n]
        where d' is the reverse of d"""
    d.reverse()
    n = len(d)
    #  [L..R] interval with max R such that d[L..R] is a prefix of d
    L = 0
    R = 0
    z = [0] * n
    for i in range(1, n):
        if i > R:  # we are outside the interval so we must compute a new one
            L = R = i
            while R < n and d[R-L] == d[R]:
                R += 1
            z[i] = R-L
            R -= 1
        else:
            k = i-L  # d[L..R] = d[1..R-L], therefore d[i..R] = d[i-L..R-L]
            if z[k] < R-i+1:  # the prefix starting at d[i] ends before the end of the interval
                z[i] = z[k]
            else:
                L = i
                while R < n and d[R-L] == d[R]:
                    R += 1
                z[i] = R-L
                R -= 1
    index_max = max(range(len(z)), key=z.__getitem__)

    print(d[:index_max][::-1])
    print("size of the period : {}".format(index_max))
    return d[:index_max]


def main():
    if len(sys.argv) != 3:
        print("Usage: python period.py [word] [n]")
        return
    w = sys.argv[1]
    n = int(sys.argv[2])

    r = calcul_r(w*n)
    z_algo(d_vector(r))


if __name__ == "__main__":
    main()
