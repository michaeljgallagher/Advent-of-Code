def parse_input():
    with open("24.txt", "r") as file:
        data = file.read()
    return data.splitlines()


def part_one():
    grid = parse_input()
    seen = set()
    seen.add("".join(grid))
    while True:
        bugs = set()
        adj = [[0] * 5 for _ in range(5)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == "#":
                    bugs.add((i, j))
                    for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                        if 0 <= ni < 5 and 0 <= nj < 5:
                            adj[ni][nj] += 1
        ngrid = [[None] * 5 for _ in range(5)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == "#" and adj[i][j] == 1:
                    ngrid[i][j] = "#"
                elif v == "." and adj[i][j] in (1, 2):
                    ngrid[i][j] = "#"
                else:
                    ngrid[i][j] = "."
        cur = "".join("".join(row) for row in ngrid)
        if cur in seen:
            return int(cur.replace("#", "1").replace(".", "0")[::-1], 2)
        seen.add(cur)
        grid = ngrid


def get_neis(level, i, j):
    neis = []
    for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
        ni, nj = i + di, j + dj
        if 0 <= ni < 5 and 0 <= nj < 5 and (ni, nj) != (2, 2):
            neis.append((level, ni, nj))
        elif ni < 0:
            neis.append((level - 1, 1, 2))
        elif ni >= 5:
            neis.append((level - 1, 3, 2))
        elif nj < 0:
            neis.append((level - 1, 2, 1))
        elif nj >= 5:
            neis.append((level - 1, 2, 3))
        elif (ni, nj) == (2, 2):
            if di == -1:
                neis.extend([(level + 1, 4, c) for c in range(5)])
            elif di == 1:
                neis.extend([(level + 1, 0, c) for c in range(5)])
            elif dj == -1:
                neis.extend([(level + 1, r, 4) for r in range(5)])
            elif dj == 1:
                neis.extend([(level + 1, r, 0) for r in range(5)])
    return neis


def part_two():
    grid = parse_input()
    bugs = set()
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == "#" and (i, j) != (2, 2):
                bugs.add((0, i, j))
    for _ in range(200):
        adj_count = {}
        if bugs:
            min_level = min(level for level, _, _ in bugs) - 1
            max_level = max(level for level, _, _ in bugs) + 1
        else:
            min_level, max_level = 0, 0
        for level in range(min_level, max_level + 1):
            for i in range(5):
                for j in range(5):
                    if (i, j) == (2, 2):
                        continue
                    pos = (level, i, j)
                    count = 0
                    for neighbor in get_neis(level, i, j):
                        if neighbor in bugs:
                            count += 1
                    adj_count[pos] = count
        new_bugs = set()
        for pos, count in adj_count.items():
            if pos in bugs and count == 1:
                new_bugs.add(pos)
            elif pos not in bugs and count in (1, 2):
                new_bugs.add(pos)
        bugs = new_bugs
    return len(bugs)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
