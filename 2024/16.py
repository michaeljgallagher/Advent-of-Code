import heapq
import math
from collections import defaultdict


def parse_input():
    with open("16.txt", "r") as file:
        data = file.read()
    grid = data.splitlines()
    n, m = len(grid), len(grid[0])
    start = end = None
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == "S":
                start = (i, j)
            if v == "E":
                end = (i, j)
    return grid, n, m, start, end


GRID, N, M, START, END = parse_input()


def solve(pt2=False):
    scores = defaultdict(lambda: math.inf)
    i, j = START
    di, dj = 0, 1
    pq = [(0, i, j, di, dj, [(i, j)])]
    res = math.inf
    all_tiles = []
    while pq:
        score, i, j, di, dj, tiles = heapq.heappop(pq)
        if (i, j) == END:
            if not pt2:
                return score
            res = min(res, score)
            if score == res:
                all_tiles.extend(tiles)
        for nscore, ni, nj, ndi, ndj in (
            (score + 1, i + di, j + dj, di, dj),
            (score + 1001, i - dj, j + di, -dj, di),
            (score + 1001, i + dj, j - di, dj, -di),
        ):
            if (
                0 <= ni < N
                and 0 <= nj < M
                and GRID[ni][nj] != "#"
                and (
                    scores[ni, nj, ndi, ndj] >= nscore
                    if pt2
                    else scores[ni, nj, ndi, ndj] > nscore
                )
            ):
                scores[ni, nj, ndi, ndj] = nscore
                heapq.heappush(pq, (nscore, ni, nj, ndi, ndj, tiles + [(ni, nj)]))
    return len(set(all_tiles))


def part_one():
    return solve()


def part_two():
    return solve(True)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
