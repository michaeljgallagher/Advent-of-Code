from math import prod

import networkx as nx

with open("25.txt", "r") as file:
    data = file.read().strip()


def part_one():
    G = nx.Graph()
    for row in data.split("\n"):
        u, vs = row.split(": ")
        for v in vs.split(" "):
            G.add_edge(u, v)
    cuts = nx.minimum_edge_cut(G)
    G.remove_edges_from(cuts)
    return prod(map(len, nx.connected_components(G)))


print(f"Part 1: {part_one()}")  # 552682
