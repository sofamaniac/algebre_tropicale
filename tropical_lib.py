# on travaille avec des numpy array
import numpy as np


def matrix_multiplication(a: np.array, b: np.array) -> np.array:
    """Multiplie deux matrices dans l'alèbre tropicale min, +"""
    assert a.ndim == 2, "Il faut des matrices à 2 dimensions"
    assert b.ndim == 2, "Il faut des matrices à 2 dimensions"
    n, ay = a.shape
    l, m = b.shape
    assert ay == l, \
        f"Dimensions compatible pour la multiplication\nVous tenter de multiplier une matrice ({n, ay}) par une matice ({l, m})"
    c = np.full((n, m), np.Inf)
    for i in range(n):
        c[i] = (a[i] + b.transpose()).min(1)
    return c


def power(m: np.array, n: int) -> np.array:
    """Renvoie m^n"""
    assert n >= 1, "n doit être supérieur à 1"
    if n == 1:
        return m
    elif n % 2 == 1:
        return matrix_multiplication(m, power(matrix_multiplication(m, m), n // 2))
    else:
        return power(matrix_multiplication(m, m), n // 2)


def calcul_r(u: str) -> np.array:
    """Calcule du r-vecteur de u"""
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


def calcul_l(u: str) -> np.array:
    """Calcule du l-vecteur de u"""
    return calcul_r(u[::-1])[::-1]


def calcul_m(u: str) -> int:
    """Calcul m(u)"""
    r_vec = calcul_r(u)
    l_vec = calcul_l(u)
    return 1 + np.max(r_vec + l_vec)
