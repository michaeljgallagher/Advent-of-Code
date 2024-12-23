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
    res = set()
    for u in filter(lambda x: x.startswith("t"), G.keys()):
        for v in filter(lambda x: x != u, G[u]):
            for w in filter(lambda x: x not in [u, v], G[u]):
                if w in G[v]:
                    cur = tuple(sorted([u, v, w]))
                    res.add(cur)
    return len(res)


def part_two():
    def bron_kerbosch(r, p, x, cur):
        if not p and not x:
            return max(r, cur, key=len)
        pivot = next(iter(p | x))
        for v in list(p - set(G[pivot])):
            cur = max(
                cur, bron_kerbosch(r | {v}, p & set(G[v]), x & set(G[v]), cur), key=len
            )
            p -= {v}
            x |= {v}
        return cur

    return ",".join(sorted(bron_kerbosch(set(), set(G.keys()), set(), set())))


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
