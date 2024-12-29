import math


def parse_input():
    with open("11.txt", "r") as file:
        data = file.read()
    serial_number = int(data)
    grid = [
        [
            ((((y * (x + 10)) + serial_number) * (x + 10)) // 100 % 10) - 5
            for y in range(1, 301)
        ]
        for x in range(1, 301)
    ]
    acc = [[0] * 300 for _ in range(300)]
    for x in range(300):
        for y in range(300):
            acc[x][y] = grid[x][y]
            if x > 0:
                acc[x][y] += acc[x - 1][y]
            if y > 0:
                acc[x][y] += acc[x][y - 1]
            if x > 0 and y > 0:
                acc[x][y] -= acc[x - 1][y - 1]
    return acc


ACC = parse_input()


def calc_power(sz):
    power = -math.inf
    res = (0, 0, sz, power)
    for x in range(300 - sz + 1):
        for y in range(300 - sz + 1):
            total = ACC[x + sz - 1][y + sz - 1]
            if x > 0:
                total -= ACC[x - 1][y + sz - 1]
            if y > 0:
                total -= ACC[x + sz - 1][y - 1]
            if x > 0 and y > 0:
                total += ACC[x - 1][y - 1]
            if total > power:
                power = total
                res = (x + 1, y + 1, sz, power)
    return res


def part_one():
    return ",".join(map(str, calc_power(3)[:2]))


def part_two():
    return ",".join(
        map(str, max((calc_power(sz) for sz in range(1, 301)), key=lambda x: x[3])[:3])
    )


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
