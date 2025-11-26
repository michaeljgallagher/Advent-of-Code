from collections import defaultdict, deque
from string import ascii_uppercase as letters


def parse_input():
    with open("20.txt", "r") as file:
        data = file.read()
    return data.splitlines()


GRID = parse_input()
N, M = len(GRID), len(GRID[0])


def find_portal(i, j):
    for di, dj in [(0, 1), (1, 0)]:
        ni, nj = i + di, j + dj
        if ni < N and nj < M and GRID[ni][nj].isupper():
            name = GRID[i][j] + GRID[ni][nj]
            for r, c in [(i - di, j - dj), (ni + di, nj + dj)]:
                if 0 <= r < N and 0 <= c < M and GRID[r][c] == ".":
                    return ((r, c), name)


def find_warps_and_termini():
    portals = defaultdict(list)
    for i, row in enumerate(GRID):
        for j, v in enumerate(row):
            if v in letters:
                cur = find_portal(i, j)
                if cur is None:
                    continue
                coord, portal = cur
                portals[portal].append(coord)
    warps = {}
    for k, v in portals.items():
        if k in ("AA", "ZZ"):
            continue
        warps[v[0]] = v[1]
        warps[v[1]] = v[0]
    return portals["AA"][0], portals["ZZ"][0], warps


def solve(pt2=False):
    start, target, warps = find_warps_and_termini()
    q = deque([(0, *start)])
    seen = {(0, *start)}
    steps = 0
    while q:
        for _ in range(len(q)):
            level, i, j = q.popleft()
            if (i, j) == target and (not pt2 or level == 0):
                return steps
            for ni, nj in (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                if (
                    0 <= ni < N
                    and 0 <= nj < M
                    and GRID[ni][nj] == "."
                    and (level, ni, nj) not in seen
                ):
                    seen.add((level, ni, nj))
                    q.append((level, ni, nj))
            if (i, j) in warps:
                if pt2:
                    nlevel = (
                        level - 1 if i in (2, N - 3) or j in (2, M - 3) else level + 1
                    )
                    if nlevel < 0:
                        continue
                else:
                    nlevel = 0
                if (nlevel, *warps[(i, j)]) not in seen:
                    seen.add((nlevel, *warps[(i, j)]))
                    q.append((nlevel, *warps[(i, j)]))
        steps += 1


print(f"Part 1: {solve()}")
print(f"Part 2: {solve(pt2=True)}")
