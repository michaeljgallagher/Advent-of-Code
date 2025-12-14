import re
from collections import deque
from functools import reduce
from operator import or_

from scipy.optimize import linprog


def parse_input():
    with open("10.txt", "r") as f:
        data = f.read()
    records = re.findall(r"\[([.#]+)\]\s+(\(.*?\))\s+\{([^}]*)\}", data)
    lights = [
        int(a.translate(str.maketrans({".": "0", "#": "1"}))[::-1], 2)
        for a, _, _ in records
    ]
    buttons = [
        [
            reduce(or_, (1 << int(n) for n in pair.split(",")), 0)
            for pair in re.findall(r"\(([^)]*)\)", b)
        ]
        for _, b, _ in records
    ]
    joltages = [[int(x) for x in c.split(",")] for _, _, c in records]
    return zip(lights, buttons, joltages)


def bfs(lights, buttons):
    q = deque([0])
    seen = {0}
    res = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == lights:
                return res
            for b in buttons:
                if (nxt := cur ^ b) in seen:
                    continue
                q.append(nxt)
                seen.add(nxt)
        res += 1


def solve(buttons, joltages):
    A = [[(x >> i) & 1 for x in buttons] for i in range(len(joltages))]
    return int(linprog([1] * len(buttons), A_eq=A, b_eq=joltages, integrality=1).fun)


def part_one():
    return sum(bfs(lights, buttons) for lights, buttons, _ in parse_input())


def part_two():
    return sum(solve(buttons, joltages) for _, buttons, joltages in parse_input())


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
