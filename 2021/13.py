import re

with open('13.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    points = [
        (int(x), int(y))
        for x, y in re.findall(r'(\d+),(\d+)', raw_data)
    ]
    folds = [
        (axis, int(n))
        for axis, n in re.findall(r'fold along ([xy])=(\d+)', raw_data)
    ]
    return points, folds


POINTS, FOLDS = parse_input(raw_data)


def make_fold(axis, line, points):
    res = set()
    if axis == 'x':
        for x, y in points:
            nx = 2 * line - x if x > line else x
            res.add((nx, y))
    else:
        for x, y in points:
            ny = 2 * line - y if y > line else y
            res.add((x, ny))
    return res


def part_one():
    return len(make_fold(*FOLDS[0], set(POINTS)))


def part_two():
    points = set(POINTS)
    for fold in FOLDS:
        axis, line = fold
        points = make_fold(axis, line, points)

    max_x, max_y = max(x for x, _ in points), max(y for _, y in points)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for j, i in points:
        grid[i][j] = '#'

    for row in grid:
        print(''.join(row))


print(f"Part 1: {part_one()}")  # 701
print(f"Part 2: {part_two()}")  # FPEKBEJL
