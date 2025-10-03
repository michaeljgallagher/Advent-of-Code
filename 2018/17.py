import re
from math import inf

SPRING_X, SPRING_Y = 500, 0


def parse_input():
    clay = set()
    xmin, xmax, ymin, ymax = inf, -inf, inf, -inf
    with open("17.txt", "r") as file:
        for line in file.read().splitlines():
            axis, v1, rlo, rhi = re.match(
                r"([xy])=(\d+), [xy]=(\d+)\.\.(\d+)", line.strip()
            ).groups()
            v1, rlo, rhi = int(v1), int(rlo), int(rhi)
            for v2 in range(rlo, rhi + 1):
                x = v1 if axis == "x" else v2
                y = v1 if axis == "y" else v2
                clay.add((x, y))
                xmin, xmax = min(xmin, x), max(xmax, x)
                ymin, ymax = min(ymin, y), max(ymax, y)
    xmin, xmax, ymin = xmin - 1, xmax + 1, ymin - 1
    return clay, xmin, xmax, ymin, ymax


def build_world(clay, xmin, xmax, ymin, ymax):
    W, H = xmax - xmin + 1, ymax - ymin + 1
    world = [["."] * W for _ in range(H)]
    for x, y in clay:
        world[y - ymin][x - xmin] = "#"
    return world


def simulate(world, xmin, ymin):
    H, W = len(world), len(world[0])

    def fall_from(x, y):
        while y + 1 < H and world[y + 1][x] in ".|":
            y += 1
            if world[y][x] == ".":
                world[y][x] = "|"
        if y + 1 >= H:
            return None
        return y

    def scan_side(x, y, step):
        xi = x
        while True:
            if world[y][xi] in ".|":
                world[y][xi] = "|"
            if y + 1 < H and world[y + 1][xi] in ".|":
                return xi, True
            nxt = xi + step
            if not (0 <= nxt < W):
                return xi, True
            if world[y][nxt] == "#":
                return xi, False
            xi = nxt

    tasks = set()
    sx, sy = SPRING_X - xmin, SPRING_Y - ymin
    tasks.add(("fall", sx, sy))

    while tasks:
        kind, x, y = tasks.pop()
        if kind == "fall":
            stop_y = fall_from(x, y)
            if stop_y is not None:
                tasks.add(("spread", x, stop_y))
        else:
            lx, left_open = scan_side(x, y, -1)
            rx, right_open = scan_side(x, y, +1)
            if not left_open and not right_open:
                for xi in range(lx, rx + 1):
                    world[y][xi] = "~"
                if y > 0:
                    tasks.add(("spread", x, y - 1))
            else:
                if left_open and y < H - 1:
                    tasks.add(("fall", lx, y))
                if right_open and y < H - 1:
                    tasks.add(("fall", rx, y))
    return world


def part_one():
    clay, xmin, xmax, ymin, ymax = parse_input()
    world = build_world(clay, xmin, xmax, ymin, ymax)
    world = simulate(world, xmin, ymin)
    return sum(val in "|~" for row in world[2:] for val in row)


def part_two():
    clay, xmin, xmax, ymin, ymax = parse_input()
    world = build_world(clay, xmin, xmax, ymin, ymax)
    world = simulate(world, xmin, ymin)
    return sum(val in "~" for row in world[2:] for val in row)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
