import re
from collections import Counter

with open('22.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    res = []
    for line in raw_data.split('\n'):
        state = int(line.split()[0] == 'on')
        x0, x1, y0, y1, z0, z1 = map(int, re.findall('-?\d+', line))
        res.append((state, x0, x1, y0, y1, z0, z1))
    return res


DATA = parse_input(raw_data)


def intersect(cube_a, cube_b):
    x0, x1, y0, y1, z0, z1 = cube_a
    i0, i1, j0, j1, k0, k1 = cube_b
    x_s, y_s, z_s = (
        max(a, b) for a, b in
        zip((x0, y0, z0), (i0, j0, k0))
    )
    x_e, y_e, z_e = (
        min(a, b) for a, b in
        zip((x1, y1, z1), (i1, j1, k1))
    )
    if x_s <= x_e and y_s <= y_e and z_s <= z_e:
        return x_s, x_e, y_s, y_e, z_s, z_e
    return False


def toggle_cubes(step, cubes):
    state, cur = step[0], step[1:]
    new = Counter()
    for cube in cubes:
        intsct = intersect(cur, cube)
        if intsct:
            new[intsct] -= cubes[cube]
    if state:
        cubes[cur] = 1
    cubes.update(new)
    return cubes


def calc_toggled(cubes):
    res = 0
    for k, v in cubes.items():
        x0, x1, y0, y1, z0, z1 = k
        size = (x1 + 1 - x0) * (y1 + 1 - y0) * (z1 + 1 - z0)
        res += size * v
    return res


def part_one(steps):
    cubes = Counter()
    for step in steps:
        state, cur = step[0], step[1:]
        cur = intersect(cur, (-50, 50, -50, 50, -50, 50))
        if not cur:
            continue
        cubes = toggle_cubes((state, *cur), cubes)
    return calc_toggled(cubes)


def part_two(steps):
    cubes = Counter()
    for step in steps:
        cubes = toggle_cubes(step, cubes)
    return calc_toggled(cubes)


print(f'Part 1: {part_one(DATA)}')  # 607657
print(f'Part 2: {part_two(DATA)}')  # 1187742789778677
