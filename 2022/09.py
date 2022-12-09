import re

with open("09.txt", "r") as file:
    data = file.read().strip()

STEPS = [(x, int(y)) for x, y in re.findall(r"(\w) (\d+)", data)]

DIRS = {
    "U": -1j,
    "D": 1j,
    "L": -1,
    "R": 1,
}


def update(rope, i, dir):
    sgn = lambda x: complex(
        (x.real > 0) - (x.real < 0), (x.imag > 0) - (x.imag < 0)
    )
    head, tail = rope[i - 1], rope[i]
    dpos = head - tail
    if abs(dpos) > abs(1 + 1j):
        rope[i] += sgn(dpos)
    return rope


def solve(knots):
    rope = [0] * knots
    seen = set()
    for dir, dist in STEPS:
        seen.add(rope[-1])
        for _ in range(dist):
            rope[0] += DIRS[dir]
            for i in range(1, knots):
                rope = update(rope, i, dir)
            seen.add(rope[-1])
    return len(seen)


print(f"Part 1: {solve(2)}")  # 6339
print(f"Part 2: {solve(10)}")  # 2541
