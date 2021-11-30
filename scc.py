import numpy as np
from matrice import calcul_matrix
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




def main():

    if len(sys.argv) < 2:
        exit(1)

    m = calcul_matrix(sys.argv[1])
    print(tarjan(m))

if __name__ == "__main__":
    main()


