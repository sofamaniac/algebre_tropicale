def tropical_power(m: np.array, n: int):
    """Calcule de m ** n dans l'algèbre tropicale
    attention renvoie une array avec des éléments de l'anneaux T"""
    T = TropicalSemiring(ZZ, use_min=True)
    t = np.vectorize(T)
    return np.linalg.matrix_power(t(m), n)
