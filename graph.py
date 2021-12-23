import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys
from matrice import calcul_matrix
from tropical_lib import calcul_r, calcul_l


def draw_graph(word):
    m = calcul_matrix(word)
    m[m == np.inf] = 0
    g = nx.convert_matrix.from_numpy_matrix(m, create_using=nx.DiGraph)

    pos = nx.circular_layout(g)
    weights = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_nodes(g, pos, node_size=200)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edges(g, pos, width=1, arrowstyle="-|>", arrows=True)
    nx.draw_networkx_edge_labels(g, pos, weights)
    plt.show()


def to_base(n, base=2):
    """Ecrit le nombre n en base base,
    permet d'itérer sur les mots d'un alphabet à base lettres"""
    res = ""
    while n:
        n, r = divmod(n, base)
        res = chr(r + 65) + res
    return res


def plot_r_l_m(word: str, n=10, max_period=2):
    """Affiche r, l et r + l pour le mot word * n,
    on doit donner dans max_period le ppcm de toutes les périodes possibles du mot pour pouvoir calculer les coubes de tendance,
    de plus il faut n > 3 * max_period + temps de transition"""
    r = calcul_r(word * n)
    l = calcul_l(word * n)

    ar = pente(r, max_period * len(word))
    al = -pente(l[::-1], max_period * len(word))

    rl = r + l
    i = rl.max()
    plt.plot(range(len(word) * n), r, label="r", color="blue")
    plt.plot(range(len(word) * n), ar * np.arange(len(word) * n), label=f"r-tendance {ar * len(word)}", color="blue", alpha=0.5)
    plt.plot(range(len(word) * n), l, label="l", color="orange")
    plt.plot(range(len(word) * n), al * np.arange(len(word) * n) + l.max(), label=f"l-tendance {al * len(word)}", color="orange", alpha=0.5)
    plt.plot(range(len(word) * n), rl, label="r + l")
    # plt.axhline(i, label="m - 1", color='red', alpha=0.5)
    plt.title(word)
    plt.legend()
    plt.show()


def pente(vec: np.array, period: int):
    """Calcule la pente moyenne de vec sur 2 period
    on doit donner dans period le ppcm de toutes les périodes possibles du mot pour pouvoir calculer les coubes de tendance,
    de plus il faut len(vec) > 3 * period + temps de transition"""
    assert (
        (vec[-period:] - vec[-2 * period: -period])
        ==
        (vec[-2 * period: -period] - vec[-3 * period: -2 * period])
            ).all(), f"Le vecteur n'est pas périodique de période {period}"
    return (vec[-1] - vec[-period - 1]) / period


def pente_equal(word: str, n=10, max_period=2):
    """Vérifie la conjecture sur l'égalité des pentes"""
    r = calcul_r(word * n)
    l = calcul_l(word * n)

    try:
        ar = pente(r, max_period * len(word))
    except AssertionError:
        input(f"{word} n'est a priori pas de période qui divise {max_period}")
    al = pente(l[::-1], max_period * len(word))

    return ar == al


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)

    draw_graph(sys.argv[1])
