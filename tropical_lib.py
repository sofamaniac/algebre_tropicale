# on travaille avec des numpy array
import numpy as np


def mut_mul(a: np.array, b: np.array) -> np.array:
    """Multiplie deux matrices dans l'alèbre tropicale min, +"""
    n, ay = np.shape(a)
    l, m = np.shape(b)
    assert ay == l, "Dimensions compatible pour la multiplication"
    c = np.full((n, m), np.Inf)
    for i in range(n):
        for j in range(m):
            c[i, j] = (a[i, :] + b[:, j]).min()
    return c


def power(m: np.array, n: int) -> np.array:
    if n == 1:
        return m
    elif n % 2 == 1:
        return mut_mul(m, power(mut_mul(m, m), n // 2))
    else:
        return power(mut_mul(m, m), n // 2)
