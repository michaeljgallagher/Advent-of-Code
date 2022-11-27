from collections import defaultdict, deque
from itertools import permutations

with open("24.txt", "r") as file:
    data = file.read().strip()


def get_points(data):
    return [
        (int(c), i, j)
        for i, row in enumerate(data.split("\n"))
        for j, c in enumerate(row)
        if c.isdigit()
    ]


def bfs(grid, start, end):
    n, m = len(grid), len(grid[0])
    q = deque([(start, 0)])
    seen = set()
    while q:
        (i, j), dist = q.popleft()
        if (i, j) == end:
            return dist
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if (
                0 > ni
                or ni >= n
                or 0 > nj
                or nj >= m
                or (ni, nj) in seen
                or grid[ni][nj] == "#"
            ):
                continue
            seen.add((ni, nj))
            q.append(((ni, nj), dist + 1))
    return -1


def build_graph(grid, points):
    graph = defaultdict(dict)
    for n, i, j in points:
        for m, k, l in points:
            if n == m:
                continue
            dist = bfs(grid, (i, j), (k, l))
            graph[n][m] = dist
            graph[m][n] = dist
    return graph


def solve(data, pt2=False):
    points = get_points(data)
    grid = [list(line) for line in data.split("\n")]
    graph = build_graph(grid, points)
    res = float("inf")
    for p in permutations(range(1, 8)):
        node = cur = 0
        for nei in p:
            cur += graph[node][nei]
            node = nei
        cur += graph[node][0] * pt2
        res = min(res, cur)
    return res


print(f"Part 1: {solve(data)}")  # 498
print(f"Part 2: {solve(data, True)}")  # 804
