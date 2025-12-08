import re
from itertools import combinations
from math import dist, prod


def parse_input():
    with open("08.txt", "r") as f:
        data = f.read()
    nodes = [
        (int(x[0]), int(x[1]), int(x[2]))
        for x in re.findall(r"(\d+),(\d+),(\d+)", data)
    ]
    edges = sorted(combinations(nodes, 2), key=lambda x: dist(x[0], x[1]))
    return nodes, edges


NODES, EDGES = parse_input()


class DSU:
    def __init__(self, nodes):
        self.n = len(nodes)
        self.parent = {u: u for u in nodes}
        self.size = dict.fromkeys(nodes, 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.size[pu] += self.size[pv]
        self.n -= 1


def part_one():
    dsu = DSU(NODES)
    for u, v in EDGES[:1000]:
        dsu.union(u, v)
    roots = {dsu.find(u) for u in dsu.parent}
    sizes = sorted(dsu.size[r] for r in roots)
    return prod(sizes[-3:])


def part_two():
    dsu = DSU(NODES)
    for u, v in EDGES:
        dsu.union(u, v)
        if dsu.n == 1:
            return u[0] * v[0]


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
