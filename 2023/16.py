from collections import deque
from functools import reduce

with open("16.txt", "r") as file:
    data = file.read().strip()

GRID = data.split("\n")


def solve(grid, i, j, di, dj):
    n, m = len(grid), len(grid[0])
    q = deque([(i, j, di, dj)])
    seen = set()
    while q:
        i, j, di, dj = q.popleft()
        if 0 > i or i >= n or 0 > j or j >= m or (i, j, di, dj) in seen:
            continue
        seen.add((i, j, di, dj))
        match grid[i][j]:
            case "/":
                q.append((i - dj, j - di, -dj, -di))
            case "\\":
                q.append((i + dj, j + di, dj, di))
            case "|" if dj:
                q.append((i + 1, j, 1, 0))
                q.append((i - 1, j, -1, 0))
            case "-" if di:
                q.append((i, j + 1, 0, 1))
                q.append((i, j - 1, 0, -1))
            case _:
                q.append((i + di, j + dj, di, dj))
    return len(set((i, j) for i, j, _, _ in seen))


def part_one():
    return solve(GRID, 0, 0, 0, 1)


def part_two():
    n, m = len(GRID), len(GRID[0])
    starts = (
        [(x, 0, 0, 1) for x in range(n)]
        + [(x, m - 1, 0, -1) for x in range(n)]
        + [(0, x, 1, 0) for x in range(m)]
        + [(n - 1, x, -1, 0) for x in range(m)]
    )
    return reduce(lambda res, start: max(res, solve(GRID, *start)), starts, 0)


print(f"Part 1: {part_one()}")  # 7074
print(f"Part 2: {part_two()}")  # 7530
