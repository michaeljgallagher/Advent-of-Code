import re
from itertools import permutations

with open("09.txt", "r") as file:
    raw_data = file.read().strip().split("\n")


def parse_input(raw_data):
    res = []
    for line in raw_data:
        u, v, w = re.findall(r"(\w+) to (\w+) = (\d+)", line)[0]
        res.append((u, v, int(w)))
    return res


DATA = parse_input(raw_data)


def build_graph(data):
    g = dict()
    nodes = set()
    for u, v, w in data:
        g[(u, v)] = w
        g[(v, u)] = w
        nodes.add(u)
        nodes.add(v)
    return g, nodes


G, NODES = build_graph(DATA)


def part_one():
    res = float("inf")
    for path in permutations(NODES):
        cur = 0
        for edge in zip(path, path[1:]):
            cur += G[edge]
        res = min(res, cur)
    return res


def part_two():
    res = 0
    for path in permutations(NODES):
        cur = 0
        for edge in zip(path, path[1:]):
            cur += G[edge]
        res = max(res, cur)
    return res


print(f"Part 1: {part_one()}")  # 117
print(f"Part 2: {part_two()}")  # 909
