import math
import re
from collections import Counter
from itertools import batched


def parse_input():
    with open("06.txt", "r") as file:
        data = file.read()
    return list(batched(map(int, re.findall(r"\d+", data)), 2))


COORDS = parse_input()
N, M = max((i for i, _ in COORDS)), max((j for _, j in COORDS))


def nearest(i, j):
    res = math.inf
    coords = []
    for x, y in COORDS:
        distance = abs(i - x) + abs(j - y)
        if distance < res:
            res = distance
            coords = [(x, y)]
        elif distance == res:
            coords.append((x, y))
    return coords[0] if len(coords) == 1 else (-1, -1)


def part_one():
    areas = Counter()
    edges = set()
    for i in range(N + 1):
        for j in (0, M):
            x, y = nearest(i, j)
            if (x, y) != (-1, -1):
                edges.add((x, y))
    for j in range(M + 1):
        for i in (0, N):
            x, y = nearest(i, j)
            if (x, y) != (-1, -1):
                edges.add((x, y))
    for i in range(N + 1):
        for j in range(M + 1):
            x, y = nearest(i, j)
            if (x, y) == (-1, -1) or (x, y) in edges:
                continue
            areas[(x, y)] += 1
    return max(areas.values())


def part_two():
    return sum(
        sum(abs(i - x) + abs(j - y) for x, y in COORDS) < 10000
        for i in range(N + 1)
        for j in range(M + 1)
    )


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
