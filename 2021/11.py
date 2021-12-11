from itertools import product

with open("11.txt", "r") as file:
    raw_data = file.read()


def parse_input(raw_data):
    res = []
    for row in raw_data.split("\n"):
        res.append(list(map(int, row)))
    return res


DATA = parse_input(raw_data)
N, M = len(DATA), len(DATA[0])


def flash(i, j, flashed):
    DATA[i][j] = 0
    flashed.add((i, j))
    for di, dj in filter(any, product([-1, 0, 1], repeat=2)):
        ni, nj = i + di, j + dj
        if (
            0 <= ni < N and
            0 <= nj < M and
            (ni, nj) not in flashed
        ):
            DATA[ni][nj] += 1
            if DATA[ni][nj] == 10:
                flash(ni, nj, flashed)


def step():
    flashed = set()
    for i in range(N):
        for j in range(M):
            if (i, j) not in flashed:
                DATA[i][j] += 1
                if DATA[i][j] == 10:
                    flash(i, j, flashed)
    return flashed


def part_one():
    res = 0
    for _ in range(100):
        res += len(step())
    return res


def part_two():
    res = 0
    while True:
        res += 1
        flashed = step()
        if len(flashed) == N * M:
            return res


print(f"Part 1: {part_one()}")  # 1688

DATA = parse_input(raw_data)

print(f"Part 2: {part_two()}")  # 403
