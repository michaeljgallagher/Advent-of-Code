import re
from collections import Counter
from copy import deepcopy

with open("07.txt", "r") as file:
    data = file.read().strip()


def parse_input(data):
    res = {}
    for k, w, v in re.findall(r"(\w+) \((\d+)\)(?: -> (.+))?", data):
        if v:
            v = v.split(", ")
            res[k] = [int(w), v]
        else:
            res[k] = (int(w), [])
    return res


GRAPH = parse_input(data)


def calc_weight(g, node):
    w, neis = g[node]
    if not neis:
        return w
    new_w = w + sum(calc_weight(g, nei) for nei in neis)
    g[node][0] = new_w
    return new_w


def part_one(g):
    indegrees = Counter()
    for k, (w, neis) in g.items():
        for nei in neis:
            indegrees[nei] += 1
    return list(set(g.keys()) - set(indegrees.keys()))[0]


def part_two(g):
    cur = part_one(g)
    g2 = deepcopy(g)
    calc_weight(g2, cur)
    diff = 0
    neis = g2[cur][1]
    while neis:
        nneis = None
        c = Counter(g2[nei][0] for nei in neis)
        if len(c) == 1:
            return g[cur][0] - diff
        common = c.most_common()[0][0]
        for nei in neis:
            if g2[nei][0] != common:
                diff = g2[nei][0] - common
                cur = nei
                nneis = g2[nei][1]
        neis = nneis


print(f"Part 1: {part_one(GRAPH)}")  # dgoocsw
print(f"Part 2: {part_two(GRAPH)}")  # 1275
