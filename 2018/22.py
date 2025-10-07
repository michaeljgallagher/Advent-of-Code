import heapq
import re
from collections import defaultdict
from functools import cache
from math import inf


def parse_input():
    with open("22.txt", "r") as file:
        data = file.read()
    depth = int(next(re.finditer(r"depth: (\d+)", data)).group(1))
    x, y = map(int, next(re.finditer(r"target: (\d+,\d+)", data)).group(1).split(","))
    return depth, x, y


DEPTH, X, Y = parse_input()


@cache
def dp(i, j):
    if (i, j) == (0, 0) or (i, j) == (X, Y):
        gi = 0
    elif i == 0:
        gi = j * 48271
    elif j == 0:
        gi = i * 16807
    else:
        gi = dp(i - 1, j) * dp(i, j - 1)
    return (gi + DEPTH) % 20183


def part_one():
    return sum(sum(dp(i, j) % 3 for j in range(Y + 1)) for i in range(X + 1))


def part_two():
    seen = defaultdict(lambda: inf)
    heap = [(0, 0, 0, 0)]
    while heap:
        d, i, j, tool = heapq.heappop(heap)
        if (i, j, tool) == (X, Y, 0):
            return d
        if seen[(i, j, tool)] <= d:
            continue
        seen[(i, j, tool)] = d
        rtype = dp(i, j) % 3
        ntool = (tool + 1) % 3 if tool == rtype else rtype
        if seen[(i, j, ntool)] > d + 7:
            heapq.heappush(heap, (d + 7, i, j, ntool))
        for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
            if ni < 0 or nj < 0:
                continue
            nrtype = dp(ni, nj) % 3
            if tool not in (nrtype, (nrtype + 1) % 3):
                continue
            if seen[(ni, nj, tool)] <= d + 1:
                continue
            heapq.heappush(heap, (d + 1, ni, nj, tool))


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
