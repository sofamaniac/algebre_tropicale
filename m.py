import sys
from tropical_lib import calcul_m


def main():
    if len(sys.argv) != 2:
        return "usage: m.py [word]"
    else:
        word = sys.argv[1]
        return calcul_m(word)


if __name__ == "__main__":
    print(main())
