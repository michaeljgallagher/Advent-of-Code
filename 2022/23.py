from collections import defaultdict, deque
from itertools import count


def parse_input():
    with open("23.txt", "r") as file:
        data = file.read()
    return {
        complex(j, i)
        for i, row in enumerate(data.splitlines())
        for j, v in enumerate(row)
        if v == "#"
    }


N, S, W, E = -1j, 1j, -1, 1
NE, SE, NW, SW = N + E, S + E, N + W, S + W
DIRS = N, NE, NW, S, SE, SW, W, E


def step(elves, checks):
    nxt = defaultdict(list)
    for elf in elves:
        if any(elf + di in elves for di in DIRS):
            for check in checks:
                if not any(elf + di in elves for di in check):
                    nxt[elf + check[0]].append(elf)
                    break
    for pos, npos in nxt.items():
        if len(npos) == 1:
            elves.symmetric_difference_update((npos.pop(), pos))
    checks.rotate(-1)
    return nxt


def part_one():
    elves = parse_input()
    checks = deque(((N, NE, NW), (S, SE, SW), (W, NW, SW), (E, NE, SE)))
    for _ in range(10):
        step(elves, checks)
    w = max(int(x.real) for x in elves) - min(int(x.real) for x in elves) + 1
    h = max(int(x.imag) for x in elves) - min(int(x.imag) for x in elves) + 1
    return (w * h) - len(elves)


def part_two():
    elves = parse_input()
    checks = deque(((N, NE, NW), (S, SE, SW), (W, NW, SW), (E, NE, SE)))
    for i in count(1):
        nxt = step(elves, checks)
        if not nxt:
            return i


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
