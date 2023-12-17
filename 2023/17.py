from collections import defaultdict
from heapq import heappop, heappush
from math import inf

with open("17.txt", "r") as file:
    data = file.read().strip()

GRID = data.split("\n")


def dijkstra(grid, lo, hi):
    n, m = len(grid), len(grid[0])
    dists = defaultdict(lambda: inf)
    heap = [(0, (0, 0, (0, 1))), (0, (0, 0, (1, 0)))]
    while heap:
        cost, (i, j, d) = heappop(heap)
        if (i, j) == (n - 1, m - 1):
            return cost
        if cost > dists[i, j, d]:
            continue
        di, dj = d
        for ndi, ndj in ((-dj, di), (dj, -di)):
            ncost = cost
            for dist in range(1, hi + 1):
                ni, nj = i + ndi * dist, j + ndj * dist
                if 0 <= ni < n and 0 <= nj < m:
                    ncost += int(grid[ni][nj])
                    if dist < lo:
                        continue
                    k = (ni, nj, (ndi, ndj))
                    if ncost < dists[k]:
                        dists[k] = ncost
                        heappush(heap, (ncost, k))
    return -1


print(f"Part 1: {dijkstra(GRID, 1, 3)}")  # 1155
print(f"Part 2: {dijkstra(GRID, 4, 10)}")  # 1283
