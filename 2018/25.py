import re


def parse_input():
    with open("25.txt", "r") as file:
        data = file.read()
    return [tuple(map(int, re.findall(r"-?\d+", line))) for line in data.splitlines()]


POINTS = parse_input()


def manhattan(u, v):
    return sum(abs(a - b) for a, b in zip(u, v))


def part_one():
    n = len(POINTS)
    parent = list(range(n))
    rank = [0] * n

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        pu, pv = find(u), find(v)
        if pu == pv:
            return
        if rank[pu] < rank[pv]:
            pu, pv = pv, pu
        parent[pv] = pu
        if rank[pu] == rank[pv]:
            rank[pu] += 1

    for i in range(n):
        for j in range(i + 1, n):
            if manhattan(POINTS[i], POINTS[j]) <= 3:
                union(i, j)
    return len({find(i) for i in range(n)})


print(f"Part 1: {part_one()}")
