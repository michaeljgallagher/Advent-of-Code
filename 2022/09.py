import re

with open("09.txt", "r") as file:
    data = file.read().strip()

STEPS = [(x, int(y)) for x, y in re.findall(r"(\w) (\d+)", data)]

DIRS = {
    "U": -1j,
    "D": 1j,
    "L": -1 + 0j,
    "R": 1 + 0j,
}


def update(rope, i, dir):
    head, tail = rope[i - 1], rope[i]
    dpos = tail - head
    if dpos.real == 0 or dpos.imag == 0:
        if abs(dpos.real) > 1:
            rope[i] += 1 if dpos.real < 0 else -1 if dpos.real > 0 else 0
        if abs(dpos.imag) > 1:
            rope[i] += 1j if dpos.imag < 0 else -1j if dpos.imag > 0 else 0
    elif (abs(dpos.real), abs(dpos.imag)) != (1, 1):
        rope[i] += 1 if dpos.real < 0 else -1 if dpos.real > 0 else 0
        rope[i] += 1j if dpos.imag < 0 else -1j if dpos.imag > 0 else 0
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
