import sys
from functools import reduce
from math import gcd
import networkx as nx
import numpy as np
from scipy.sparse.csgraph import connected_components
from matrice import calcul_matrix


def strongly_connected_components(m: np.array) -> list:
    """Return the list of the componnent of the graph descbed by
    the matrix m (with -inf if no edges)"""
    nb, labels = connected_components(m, connection='strong')
    return [list(np.arange(m.shape[0])[labels == i]) for i in range(nb)]


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def critical_cycles(m: np.array):
    """
    Renvoie un dictionnaire associant chaque sous-composante connexe du 
    graphe induit de la matrice à sa liste de cycle critique. Un cycle critique est représenté
    par un doublet (liste des sommets du cycle, longueur du cycle)
    """
    a = np.copy(m)

    a[a == np.inf] = 0

    # On calcule les composantes connexes
    components = strongly_connected_components(m)

    scc_to_cycle = dict()

    for c in components:
        n = len(c)
        m_ = np.full((n, n), 0)

        for i in range(0, n):
            for j in range(n):
                m_[i, j] = a[c[i], c[j]]

        g_scc = nx.convert_matrix.from_numpy_matrix(m_, create_using=nx.DiGraph)

        dic = {}
        for i in range(n):
            dic[i] = c[i]

        # On détermine les cycles dans la composante fortement connexe
        cycles = list(nx.simple_cycles(g_scc))

        min_weight = np.inf
        critic = []
        for cycle in cycles:
            weight = 0
            l = len(cycle)

            # Addition des poids d'un cycle
            for i in range(l):
                weight += m_[cycle[i], cycle[(i + 1) % l]]

            weight /= l
            if weight < min_weight:
                min_weight = weight
                critic = [(cycle, l)]

            elif weight == min_weight:
                critic.append((cycle, l))

        scc_to_cycle[tuple(c)] = critic

    return scc_to_cycle


def cyclicite(m: np.array):
    """
    Retourne la cyclité d'un graphe
    """
    # {SCC: [([Sommets composant le cycle1], longueur du cycle1), ([Sommets composant le cycle2], longueur du cycle2) ...]}
    scc = critical_cycles(m)
    l_gcd = []
    for c, v in scc.items():
        if v != []:
            # On applique le PGCD sur l'ensemble des cycles d'une SCC pour trouver la cyclicité de la composante connexe
            pgcd = reduce(gcd, [lg for avg, lg in v])
            l_gcd.append(pgcd)

    # On applique le PPCM sur la cyclicité de chaque composante connexe du graphe
    return reduce(lcm, l_gcd)


def main():
    if len(sys.argv) < 2:
        exit(1)

    m = calcul_matrix(sys.argv[1])

    cycles = critical_cycles(m)
    for scc, c in cycles.items():
        print(scc, c)
    print(f"Cyclicité du mot {sys.argv[1]} : {cyclicite(m)}")


if __name__ == "__main__":
    main()
