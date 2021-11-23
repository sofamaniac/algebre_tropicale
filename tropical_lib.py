# on travaille avec des numpy array
import numpy as np


def mut_mul(a, b):
    n = np.shape(a)[0]
    m = np.shape(b)[1]
    l = np.shape(b)[0]
    c = np.full((n, m), np.Inf)
    for i in range(n):
        for j in range(m):
            for k in range(l):
                c[i, j] = min(c[i, j], a[i, k]+b[k, j])
    return c


def power(M, n):
    if n == 1:
        return M
    elif n & 1 == 1:
        return mut_mul(M, power(mut_mul(M, M), n >> 1))
    else:
        return power(mut_mul(M, M), n >> 1)
