from itertools import count, product

with open("11.txt", "r") as file:
    raw_data = file.read()


def parse_input(raw_data):
    res = []
    for row in raw_data.split("\n"):
        res.append(list(map(int, row)))
    return res


DATA = parse_input(raw_data)
N, M = len(DATA), len(DATA[0])


def flash(i, j, grid, flashed):
    grid[i][j] = 0
    flashed.add((i, j))
    for di, dj in filter(any, product([-1, 0, 1], repeat=2)):
        ni, nj = i + di, j + dj
        if (
            0 <= ni < N and
            0 <= nj < M and
            (ni, nj) not in flashed
        ):
            grid[ni][nj] += 1
            if grid[ni][nj] == 10:
                flash(ni, nj, grid, flashed)


def step(grid):
    flashed = set()
    for i in range(N):
        for j in range(M):
            grid[i][j] += int((i, j) not in flashed)
            if grid[i][j] == 10:
                flash(i, j, grid, flashed)
    return len(flashed)


def part_one():
    grid = [row[:] for row in DATA]
    res = 0
    for _ in range(100):
        res += step(grid)
    return res


def part_two():
    grid = [row[:] for row in DATA]
    for i in count(1):
        if step(grid) == N * M:
            return i


print(f"Part 1: {part_one()}")  # 1688
print(f"Part 2: {part_two()}")  # 403
