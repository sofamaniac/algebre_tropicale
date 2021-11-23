import numpy as np
import sys
from r import calcul_r


def calcul_l(u):
    return calcul_r(u[::-1])[::-1]


def main():
    if len(sys.argv) != 2:
        return "usage: r.py [word]"
    else:
        word = sys.argv[1]
        return calcul_l(word)


if __name__ == "__main__":
    print(main())
