import re

with open('12.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    res = re.findall(r'([A-Z]+)(\d+)', data)
    return [(s, int(x)) for s, x in res]


CARDINAL = {
    0: 'E',
    90: 'S',
    180: 'W',
    270: 'N'
}

DIRS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
    'F': 1,
    'R': 1,
    'L': -1
}


def part_one(instr):
    x, y = 0, 0
    deg = 0
    for d, n in instr:
        if d in 'RL':
            deg = (deg + DIRS[d]*n) % 360
        if d in 'NESW':
            x += DIRS[d][0] * n
            y += DIRS[d][1] * n
        if d == 'F':
            x += DIRS[CARDINAL[deg]][0] * n
            y += DIRS[CARDINAL[deg]][1] * n

    return abs(x) + abs(y)


def part_two(instr):
    way_x, way_y = 10, 1
    x, y = 0, 0
    for d, n in instr:
        if d in 'RL':
            if n == 180:
                way_x, way_y = -way_x, -way_y
            if (d == 'R' and n == 90) or (d == 'L' and n == 270):
                way_x, way_y = way_y, -way_x
            if (d == 'R' and n == 270) or (d == 'L' and n == 90):
                way_x, way_y = -way_y, way_x
        if d in 'NESW':
            way_x += DIRS[d][0] * n
            way_y += DIRS[d][1] * n
        if d == 'F':
            x += way_x * n
            y += way_y * n

    return abs(x) + abs(y)

instr = parse_input(data)
print(f'Part 1: {part_one(instr)}')  # 882
print(f'Part 2: {part_two(instr)}')  # 28885
