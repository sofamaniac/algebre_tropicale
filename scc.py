import numpy as np
import networkx as nx
from matrice import calcul_matrix
from math import gcd
from functools import reduce
import sys

def tarjan(m):

    n = m.shape[0]
    index_list = [-1 for i in range(n)]
    low_link = [-1 for i in range(n)]
    on_stack = [False for i in range(n)]
    index = 0
    s = []
    result = []

    def strongConnected(v):
        nonlocal index
        index_list[v] = index
        low_link[v] = index
        index += 1
        s.append(v)
        on_stack[v] = True


        for w in range(n):
            if m[v][w] == np.inf:
                continue
            if index_list[w] == -1:
                strongConnected(w)
                low_link[v] = min(low_link[v], low_link[w])
            elif on_stack[w]:
                low_link[v] = min(low_link[v], index_list[w])

        if low_link[v] == index_list[v]:
            scc = []
            cont = True
            while cont:
                w = s.pop()
                on_stack[w] = False
                scc.append(w)
                cont = (w != v)
            result.append(scc)
    
    for i, v in enumerate(index_list):
        if v == -1:
            strongConnected(i)
    return result

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def critical_cycles(m):
    """
    Renvoie un dictionnaire associant chaque sous-composante connexe du 
    graphe induit de la matrice à sa liste de cycle critique. Un cycle critique est représenté
    par un doublet (liste des sommets du cycle, longueur du cycle)
    """
    a = np.copy(m)

    a[a == np.inf] = 0

    # On calcule les composantes connexes
    components = tarjan(m)

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

            for i in range(l):
                weight += m_[cycle[i], cycle[(i+1) % l]]
            
            weight /= l
            if weight < min_weight:
                min_weight = weight
                critic = [(cycle, l)]

            elif weight == min_weight:
                critic.append((cycle, l))


        scc_to_cycle[tuple(c)] = critic

    return scc_to_cycle

def cyclicite(m):
    """
    Retourne la cyclité d'un graphe
    """
    cycles = critical_cycles(m)
    l_gcd = []
    for c, v in cycles.items():
        if v != []:
            pgcd = reduce(gcd, [lg for avg, lg in v])
            l_gcd.append(pgcd)
    
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


