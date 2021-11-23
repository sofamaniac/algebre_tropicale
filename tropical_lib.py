# on travaille avec des numpy array
import numpy as np


def mut_mul(a: np.array, b: np.array) -> np.array:
    """Multiplie deux matrices dans l'alèbre tropicale min, +"""
    n = np.shape(a)[0]
    m = np.shape(b)[1]
    l = np.shape(b)[0]
    c = np.full((n, m), np.Inf)
    for i in range(n):
        for j in range(m):
            for k in range(l):
                c[i, j] = min(c[i, j], a[i, k] + b[k, j])
    return c


def power(m: np.array, n: int) -> np.array:
    if n == 1:
        return m
    elif n % 2 == 1:
        return mut_mul(m, power(mut_mul(m, m), n // 2))
    else:
        return power(mut_mul(m, m), n // 2)
