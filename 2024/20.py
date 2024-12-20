from collections import deque
from itertools import combinations


def parse_input():
    with open("20.txt", "r") as file:
        data = file.read()
    grid = data.splitlines()
    s = e = None
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == "S":
                s = (i, j)
            elif v == "E":
                e = (i, j)
    return grid, s, e


GRID, S, E = parse_input()
N, M = len(GRID), len(GRID[0])


def bfs():
    q = deque([(*S, [S])])
    seen = {S}
    while q:
        i, j, path = q.popleft()
        if (i, j) == E:
            return path
        for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if (
                0 <= ni < N
                and 0 <= nj < M
                and GRID[ni][nj] != "#"
                and (ni, nj) not in seen
            ):
                seen.add((ni, nj))
                q.append((ni, nj, path + [(ni, nj)]))


PATH = bfs()


def solve(cheat=2):
    path_length = len(PATH) - 1
    cost_start = {u: i for i, u in enumerate(PATH)}
    cost_end = {u: i for i, u in enumerate(reversed(PATH))}
    return sum(
        path_length - (cost_start[u] + cost_end[v] + dist) >= 100
        for u, v in combinations(PATH, 2)
        if (dist := abs(u[0] - v[0]) + abs(u[1] - v[1])) <= cheat
    )


def part_one():
    return solve()


def part_two():
    return solve(20)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
