from collections import defaultdict
from itertools import product

with open("18.txt", "r") as file:
    data = file.read().strip()

LIGHTS = [list(map(lambda x: int(x == "#"), line)) for line in data.split("\n")]


def find_on(grid):
    on = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                on.add((i, j))
    return on


def find_neighbors(points):
    neis = defaultdict(int)
    for p in points:
        for delta in filter(any, product([-1, 0, 1], repeat=2)):
            ni, nj = (x + dx for x, dx in zip(p, delta))
            if 0 <= ni < 100 and 0 <= nj < 100:
                neis[ni, nj] += 1
    return neis


def step(points):
    new_on = set()
    neis = find_neighbors(points)
    for k, v in neis.items():
        if v == 3 or (v == 2 and k in points):
            new_on.add(k)
    return new_on


def part_one():
    on = find_on(LIGHTS)
    for _ in range(100):
        on = step(on)
    return len(on)


def part_two():
    on = find_on(LIGHTS)
    on.update(((0, 0), (0, 99), (99, 0), (99, 99)))
    for _ in range(100):
        on = step(on)
        on.update(((0, 0), (0, 99), (99, 0), (99, 99)))
    return len(on)


print(f"Part 1: {part_one()}")  # 821
print(f"Part 2: {part_two()}")  # 886
