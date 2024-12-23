from collections import defaultdict


def parse_input():
    with open("23.txt", "r") as file:
        data = file.read()
    g = defaultdict(list)
    for line in data.splitlines():
        u, v = line.split("-")
        g[u].append(v)
        g[v].append(u)
    return g


G = parse_input()


def part_one():
    ts = filter(lambda x: x.startswith("t"), G.keys())
    res = set()
    for u in ts:
        for v in filter(lambda x: x != u, G[u]):
            for w in filter(lambda x: x not in [u, v], G[u]):
                if w in G[v]:
                    cur = tuple(sorted([u, v, w]))
                    res.add(cur)
    return len(res)


def part_two():
    def clique(nodes, sz):
        if sz == 0:
            return []
        for u in nodes:
            nnodes = filter(lambda v: v in G[u], nodes)
            res = clique(nnodes, sz - 1)
            if res is not None:
                return res + [u]
        return

    nodes = G.keys()
    l, r = 3, len(nodes)
    while l < r:
        m = l + (r - l >> 1)
        if clique(nodes, m) is not None:
            l = m + 1
        else:
            r = m - 1
    return ",".join(sorted(clique(nodes, l)))


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
