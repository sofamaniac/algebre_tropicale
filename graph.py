import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys

from matrice import  calcul_matrix


def draw_graph(word):
    m = calcul_matrix(word)
    m[m == np.inf] = 0
    g = nx.convert_matrix.from_numpy_matrix(m, create_using=nx.DiGraph)

    pos = nx.circular_layout(g)
    nx.draw_networkx_nodes(g, pos, node_size=200)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edges(g, pos, width=1, arrowstyle="-|>", arrows=True)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)

    draw_graph(sys.argv[1])
