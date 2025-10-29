from collections import deque
from heapq import heappop, heappush


def parse_input():
    with open("18.txt") as f:
        grid = f.readlines()
    start = (0, 0)
    keys = {}
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == "@":
                start = (i, j)
            elif v.islower():
                keys[v] = (i, j)
    return grid, start, keys


GRID, START, KEYS = parse_input()


def bfs(i, j):
    reachable = {}
    q = deque([(i, j, 0, set())])
    seen = {(i, j)}
    while q:
        i, j, dist, doors = q.popleft()
        for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
            if (ni, nj) in seen:
                continue
            if not (0 <= ni < len(GRID) and 0 <= nj < len(GRID[0])):
                continue
            cur = GRID[ni][nj]
            if cur == "#":
                continue
            seen.add((ni, nj))
            ndoors = doors.copy()
            if cur.isupper():
                ndoors.add(cur.lower())
            if cur.islower():
                reachable[cur] = (dist + 1, frozenset(ndoors))
            q.append((ni, nj, dist + 1, ndoors))
    return reachable


def part_one():
    all_keys = set(KEYS.keys())
    num_keys = len(all_keys)
    g = {"@": bfs(*START)}
    for key, pos in KEYS.items():
        g[key] = bfs(*pos)
    key_to_bit = {k: i for i, k in enumerate(sorted(all_keys))}
    all_mask = (1 << num_keys) - 1
    pq = [(0, "@", 0)]
    best = {}
    while pq:
        dist, pos, mask = heappop(pq)
        if mask == all_mask:
            return dist
        state = (pos, mask)
        if state in best:
            continue
        best[state] = dist
        for nkey, (key_dist, required_doors) in g[pos].items():
            bit = key_to_bit[nkey]
            if mask & (1 << bit):
                continue
            can_reach = all((mask & (1 << key_to_bit[door])) for door in required_doors)
            if not can_reach:
                continue
            nmask = mask | (1 << bit)
            nstate = (nkey, nmask)
            if nstate not in best:
                heappush(pq, (dist + key_dist, nkey, nmask))
    return -1


def modify_grid_part2(grid, start):
    i, j = start
    ngrid = [list(row) for row in grid]
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 or dj == 0:
                ngrid[i + di][j + dj] = "#"
    ngrid[i - 1][j - 1] = "0"
    ngrid[i - 1][j + 1] = "1"
    ngrid[i + 1][j - 1] = "2"
    ngrid[i + 1][j + 1] = "3"
    return ["".join(row) for row in ngrid]


def part_two():
    # modify grid
    global GRID
    i, j = START
    ngrid = [list(row) for row in GRID]
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 or dj == 0:
                ngrid[i + di][j + dj] = "#"
    ngrid[i - 1][j - 1] = "0"
    ngrid[i - 1][j + 1] = "1"
    ngrid[i + 1][j - 1] = "2"
    ngrid[i + 1][j + 1] = "3"
    GRID = ngrid

    robots = {}
    for i, row in enumerate(GRID):
        for j, cell in enumerate(row):
            if cell in "0123":
                robots[cell] = (i, j)
    all_keys = set(KEYS.keys())
    num_keys = len(all_keys)

    g = {}
    for robot_id, pos in robots.items():
        g[robot_id] = bfs(*pos)
    for key, pos in KEYS.items():
        g[key] = bfs(*pos)

    key_to_bit = {k: i for i, k in enumerate(sorted(all_keys))}
    all_mask = (1 << num_keys) - 1

    initial = (
        "0",
        "1",
        "2",
        "3",
    )
    pq = [(0, initial, 0)]
    best = {}

    while pq:
        dist, positions, mask = heappop(pq)
        if mask == all_mask:
            return dist
        state = (positions, mask)
        if state in best:
            continue
        best[state] = dist
        for robot_idx in range(4):
            curr_pos = positions[robot_idx]
            if curr_pos not in g:
                continue
            for nkey, (key_dist, required_doors) in g[curr_pos].items():
                bit = key_to_bit[nkey]
                if mask & (1 << bit):
                    continue
                can_reach = all(
                    (mask & (1 << key_to_bit[door])) for door in required_doors
                )
                if not can_reach:
                    continue
                npos = list(positions)
                npos[robot_idx] = nkey
                npos = tuple(npos)
                nmask = mask | (1 << bit)
                nstate = (npos, nmask)
                if nstate not in best:
                    heappush(pq, (dist + key_dist, npos, nmask))
    return -1


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
