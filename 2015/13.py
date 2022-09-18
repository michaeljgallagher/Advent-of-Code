import re
from collections import defaultdict
from itertools import permutations

with open("13.txt", "r") as file:
    raw_data = file.read().strip()


def parse_input(raw_data):
    g = defaultdict(int)
    happy = lambda sgn, w: int(w) * (1 - 2 * (sgn == "lose"))
    nodes = set()
    for u, sgn, w, v in re.findall(
        r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)", raw_data
    ):
        g[u, v] += happy(sgn, w)
        g[v, u] += happy(sgn, w)
        nodes.update((u, v))
    return g, nodes


def brute_force(g, nodes):
    res = 0
    for path in permutations(nodes):
        path = list(path)
        cur = 0
        for u, v in zip(path, path[1:] + [path[0]]):
            cur += g[u, v]
        res = max(res, cur)
    return res


def part_one():
    g, nodes = parse_input(raw_data)
    return brute_force(g, nodes)


def part_two():
    g, nodes = parse_input(raw_data)
    nodes.add("me")
    return brute_force(g, nodes)


print(f"Part 1: {part_one()}")  # 664
print(f"Part 2: {part_two()}")  # 640
