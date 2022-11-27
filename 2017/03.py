from itertools import product

SQUARE = 325489


def part_one():
    layer = 1
    while layer * layer < SQUARE:
        layer += 2
    distance = abs(SQUARE - (layer * layer - ((layer - 1) >> 1)))
    return distance + ((layer - 1) >> 1)


def spiral_sum():
    grid = {}
    grid[0, 0] = 1
    x, y = 0, 0
    dx, dy = 0, -1
    while True:
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
        grid[x, y] = sum(
            grid.get((x + dx, y + dy), 0)
            for dx, dy in filter(any, product([-1, 0, 1], repeat=2))
        )
        yield grid[x, y]


def part_two():
    return next(x for x in spiral_sum() if x > SQUARE)


print(f"Part 1: {part_one()}")  # 552
print(f"Part 2: {part_two()}")  # 330785
