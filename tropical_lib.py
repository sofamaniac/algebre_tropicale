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
