import re
from collections import defaultdict

with open("06.txt", "r") as file:
    raw_data = file.read().strip().split("\n")


def parse_input(raw_data):
    res = []
    for line in raw_data:
        x, a, b, c, d = re.findall(r"(\w+) (\d+),(\d+) through (\d+),(\d+)", line)[0]
        res.append([x, tuple(map(int, (a, b, c, d)))])
    return res


data = parse_input(raw_data)


def trigger_lights(grid, ops, cmd):
    inst, (a, b, c, d) = cmd
    if a > c:
        a, c = c, a
    if b > d:
        b, d = d, b
    f = ops[inst]
    for i in range(a, c + 1):
        for j in range(b, d + 1):
            cur = grid[(i, j)]
            grid[(i, j)] = f(cur)
    return grid


def part_one(data):
    ops = {
        "on": lambda x: 1,
        "off": lambda x: 0,
        "toggle": lambda x: 1 - x,
    }
    grid = defaultdict(int)
    for cmd in data:
        grid = trigger_lights(grid, ops, cmd)
    return sum(grid.values())


def part_two(data):
    ops = {
        "on": lambda x: x + 1,
        "off": lambda x: max(0, x - 1),
        "toggle": lambda x: x + 2,
    }
    grid = defaultdict(int)
    for cmd in data:
        grid = trigger_lights(grid, ops, cmd)
    return sum(grid.values())


print(f"Part 1: {part_one(data)}")  # 377891
print(f"Part 2: {part_two(data)}")  # 14110788
