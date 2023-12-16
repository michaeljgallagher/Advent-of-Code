from collections import deque

with open("16.txt", "r") as file:
    data = file.read().strip()

dirs = {
    "/": [1j, -1j],
    "\\": [-1j, 1j],
}


def solve(grid, i, j, d):
    n, m = len(grid), len(grid[0])
    q = deque([(i, j, d)])
    seen = set()
    while q:
        i, j, d = q.popleft()
        if 0 > i or i >= n or 0 > j or j >= m or (i, j, d) in seen:
            continue
        seen.add((i, j, d))
        cur = grid[i][j]
        if cur in ("/", "\\"):
            nd = d * dirs[cur][bool(d.real)]
            di, dj = int(nd.real), int(nd.imag)
            q.append((i + di, j + dj, nd))
        elif (cur == "|" and d.imag) or (cur == "-" and d.real):
            nd = d * 1j
            di, dj = int(nd.real), int(nd.imag)
            q.append((i + di, j + dj, nd))
            nd = d * -1j
            di, dj = int(nd.real), int(nd.imag)
            q.append((i + di, j + dj, nd))
        else:
            di, dj = int(d.real), int(d.imag)
            q.append((i + di, j + dj, d))
    return len(set((i, j) for i, j, _ in seen))


def part_one():
    grid = data.split("\n")
    return solve(grid, 0, 0, 1j)


def part_two():
    grid = data.split("\n")
    n, m = len(grid), len(grid[0])
    res = 0
    for i, j, d in (
        [(x, 0, 1j) for x in range(n)]
        + [(x, m - 1, -1j) for x in range(n)]
        + [(0, x, 1) for x in range(m)]
        + [(n - 1, x, -1) for x in range(m)]
    ):
        res = max(res, solve(grid, i, j, d))
    return res


print(f"Part 1: {part_one()}")  # 7074
print(f"Part 2: {part_two()}")  # 7530
