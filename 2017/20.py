import math
import re
from collections import defaultdict
from itertools import batched


def parse_input():
    with open("20.txt", "r") as file:
        data = file.read()
    return batched(batched(map(int, re.findall(r"(-?\d+)", data)), 3), 3)


def calc_pos(p, v, a, t):
    return tuple(np + nv * t + (na * t * (t + 1) >> 1) for np, nv, na in zip(p, v, a))


def part_one():
    particles = parse_input()
    res = 0
    low = math.inf
    for i, particle in enumerate(particles):
        cur = calc_pos(*particle, 1000)
        if (nlow := sum(abs(x) for x in cur)) < low:
            res = i
            low = nlow
    return res


def part_two():
    particles = parse_input()
    for t in range(50):
        cur = defaultdict(list)
        for particle in particles:
            npos = tuple(calc_pos(*particle, t))
            cur[npos].append(particle)
        particles = []
        for a in cur.values():
            if len(a) == 1:
                particles.extend(a)
    return len(particles)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
