import re

with open('17.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    pairs = re.findall(r'(-?\d+)..(-?\d+)', raw_data)
    return [int(x) for pair in pairs for x in pair]


MIN_X, MAX_X, MIN_Y, MAX_Y = parse_input(raw_data)


def step(x, y, dx, dy):
    x += dx
    y += dy
    dx += -1 if dx > 0 else 1 if dx < 0 else 0
    dy += -1
    return x, y, dx, dy


def run_steps(dx, dy):
    x, y = 0, 0
    while y >= MIN_Y:
        x, y, dx, dy = step(x, y, dx, dy)
        if MIN_X <= x <= MAX_X and MIN_Y <= y <= MAX_Y:
            return True
    return False


def part_one():
    return MIN_Y * (MIN_Y + 1) // 2


def part_two():
    res = 0
    for i in range(MAX_X + 1):
        for j in range(MIN_Y, -MIN_Y):
            res += run_steps(i, j)
    return res


print(f'Part 1: {part_one()}')  # 8256
print(f'Part 2: {part_two()}')  # 2326
