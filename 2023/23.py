from collections import defaultdict, deque

with open("23.txt", "r") as file:
    data = file.read().strip()

G = data.split("\n")
N, M = len(G), len(G[0])
SLOPES = {
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
}


def get_neis(i, j, pt2=False):
    c = G[i][j]
    if not pt2 and c in SLOPES:
        dirs = [SLOPES[c]]
    else:
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and G[ni][nj] != "#":
            yield ni, nj


def get_vertices():
    vertices = {(0, 1), (N - 1, M - 2)}
    for i in range(N):
        for j in range(M):
            if G[i][j] != "#" and len(list(get_neis(i, j, True))) > 2:
                vertices.add((i, j))
    dists = defaultdict(list)
    for x, y in vertices:
        q = deque([(x, y)])
        seen = {(x, y)}
        cur = 0
        while q:
            cur += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for ni, nj in get_neis(i, j, True):
                    if (ni, nj) in seen:
                        continue
                    if (ni, nj) in vertices:
                        dists[x, y].append((cur, ni, nj))
                    else:
                        q.append((ni, nj))
                    seen.add((ni, nj))
    return dists


def part_one():
    q = deque([(0, 1, set())])
    res = cur = 0
    while q:
        for _ in range(len(q)):
            i, j, seen = q.popleft()
            if (i, j) == (N - 1, M - 2):
                res = max(res, cur)
            for ni, nj in get_neis(i, j):
                if (ni, nj) not in seen:
                    q.append((ni, nj, seen | {(ni, nj)}))
        cur += 1
    return res


def part_two():
    dists = get_vertices()
    res = 0

    def dfs(i, j, seen, cur):
        nonlocal res
        if (i, j) == (N - 1, M - 2):
            res = max(res, cur)
        for dist, ni, nj in dists[i, j]:
            if (ni, nj) not in seen:
                seen.add((ni, nj))
                dfs(ni, nj, seen, cur + dist)
                seen.remove((ni, nj))

    dfs(0, 1, set(), 0)
    return res


print(f"Part 1: {part_one()}")  # 2358
print(f"Part 2: {part_two()}")  # 6586
