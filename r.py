import sys
import numpy as np


def calcul_r(u: str) -> np.array:
    n = len(u)
    # we initialize the r vector
    r = np.zeros(n, dtype=int)

    for i in range(n):  # calcul de r(u[:i], u[i])
        # for each letter c of the word u, and a prefix u' s.t. u=u'cu''
        # we look at w, first suffix of u' starting with the letter c

        # indice de la dernière occurence de u[i] dans u[:i]
        start_of_w = u.rfind(u[i], 0, i)

        if start_of_w == -1:
            r[i] = 0
        else:
            r[i] = 1 + np.min(r[start_of_w:i])
    return r


def main():
    if len(sys.argv) != 2:
        return "usage: r.py [word]"
    else:
        word = sys.argv[1]
        return calcul_r(word)


if __name__ == "__main__":
    print(main())
