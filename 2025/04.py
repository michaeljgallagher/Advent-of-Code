from itertools import product


def parse_input():
    with open("04.txt", "r") as f:
        data = f.read()
    return list(map(list, data.splitlines()))


def step(grid):
    n, m = len(grid), len(grid[0])
    res = []
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v != "@":
                continue
            cur = 0
            for di, dj in filter(any, product(range(-1, 2), repeat=2)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == "@":
                    cur += 1
            if cur < 4:
                res.append((i, j))
    return res


def part_one():
    return len(step(parse_input()))


def part_two():
    grid = parse_input()
    res = 0
    while removable := step(grid):
        for i, j in removable:
            grid[i][j] = "."
            res += 1
    return res


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
