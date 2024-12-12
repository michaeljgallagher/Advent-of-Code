def parse_input():
    with open("12.txt", "r") as file:
        data = file.read()
    return data.splitlines()


PLOTS = parse_input()
N, M = len(PLOTS), len(PLOTS[0])


def find_regions():
    seen = set()
    res = []

    def dfs(i, j, cur):
        cur.append((i, j))
        seen.add((i, j))
        for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if (
                0 <= ni < N
                and 0 <= nj < M
                and PLOTS[ni][nj] == PLOTS[i][j]
                and (ni, nj) not in seen
            ):
                dfs(ni, nj, cur)

    for i in range(N):
        for j in range(M):
            if (i, j) in seen:
                continue
            cur = []
            dfs(i, j, cur)
            if cur:
                res.append(cur)
    return res


REGIONS = find_regions()


def calc_perim(region):
    res = 0
    for i, j in region:
        c = PLOTS[i][j]
        for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 > ni or ni >= N or 0 > nj or nj >= M or PLOTS[ni][nj] != c:
                res += 1
    return res


def calc_sides(region):
    perimeter = set()
    region = set(region)
    res = 0
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for i, j in region:
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if (ni, nj) not in region:
                perimeter.add((ni - di, nj - dj, di, dj))
    while perimeter:
        i, j, di, dj = perimeter.pop()
        res += 1
        ni, nj = i - dj, j + di
        while (ni, nj, di, dj) in perimeter:
            perimeter.remove((ni, nj, di, dj))
            ni -= dj
            nj += di
        ni, nj = i + dj, j - di
        while (ni, nj, di, dj) in perimeter:
            perimeter.remove((ni, nj, di, dj))
            ni += dj
            nj -= di
    return res


def part_one():
    return sum(len(region) * calc_perim(region) for region in REGIONS)


def part_two():
    return sum(len(region) * calc_sides(region) for region in REGIONS)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
