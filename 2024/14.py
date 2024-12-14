import re
from itertools import count
from math import prod


def parse_input():
    with open("14.txt", "r") as file:
        data = file.read()
    pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    return [list(map(int, x)) for x in re.findall(pattern, data)]


ROBOTS = parse_input()
N, M = 103, 101


def step(j, i, dj, di, t):
    di *= t
    dj *= t
    i = (i + di) % N
    j = (j + dj) % M
    return i, j


def draw(positions):
    grid = [["."] * M for _ in range(N)]
    for i, j in positions:
        grid[i][j] = "\u2588"
    print("\n".join("".join(row) for row in grid))


def part_one():
    quadrants = [0] * 4
    for i, j in (step(*robot, 100) for robot in ROBOTS):
        n = (N >> 1) + 1
        m = (M >> 1) + 1
        x, r = divmod(i, n)
        y, rr = divmod(j, m)
        if r == n - 1 or rr == m - 1:
            continue
        quadrants[x * 2 + y] += 1
    return prod(quadrants)


def part_two():
    for t in count():
        cur = {step(*robot, t) for robot in ROBOTS}
        if len(cur) == len(ROBOTS):
            draw(cur)
            return t


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
