import re

with open('12.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    res = re.findall(r'([A-Z]+)(\d+)', data)
    return [(s, int(x)) for s, x in res]

DIRS = {
    'N': 0 + 1j,
    'E': 1 + 0j,
    'S': 0 + -1j,
    'W': -1 + 0j,
    'R': 0 - 1j,
    'L': 0 + 1j,
}


def part_one(instr):
    pos = 0 + 0j
    direction = 1 + 0j  # EAST
    for d, n in instr:
        if d in 'RL':
            direction *= DIRS[d] ** (n // 90)
        elif d in 'ENWS':
            pos += DIRS[d] * n
        else:  # d == 'F'
            pos += direction * n
    return abs(int(pos.real)) + abs(int(pos.imag))


def part_two(instr):
    way = 10 + 1j
    pos = 0 + 0j
    for d, n in instr:
        if d in 'RL':
            way *= DIRS[d] ** (n // 90)
        elif d in 'ENWS':
            way += DIRS[d] * n
        else:  # d == 'F'
            pos += way * n
    return abs(int(pos.real)) + abs(int(pos.imag))


instr = parse_input(data)
print(f'Part 1: {part_one(instr)}')  # 882
print(f'Part 2: {part_two(instr)}')  # 28885
