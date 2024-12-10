def parse_input():
    with open("10.txt", "r") as file:
        data = file.read()
    return [list(map(int, row)) for row in data.splitlines()]


GRID = parse_input()
N, M = len(GRID), len(GRID[0])
TRAILHEADS = [(i, j) for i in range(N) for j in range(M) if GRID[i][j] == 0]


def dfs(i, j, pt2=False):
    if GRID[i][j] == 9:
        return 1 if pt2 else {(i, j)}
    res = 0 if pt2 else set()
    for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if 0 <= ni < N and 0 <= nj < M and GRID[ni][nj] == GRID[i][j] + 1:
            if pt2:
                res += dfs(ni, nj, True)
            else:
                res |= dfs(ni, nj)
    return res


def part_one():
    return sum(len(dfs(i, j)) for i, j in TRAILHEADS)


def part_two():
    return sum(dfs(i, j, True) for i, j in TRAILHEADS)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
