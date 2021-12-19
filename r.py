import sys
from tropical_lib import  calcul_r


def main():
    if len(sys.argv) != 2:
        return "usage: r.py [word]"
    else:
        word = sys.argv[1]
        return calcul_r(word)


if __name__ == "__main__":
    print(main())
