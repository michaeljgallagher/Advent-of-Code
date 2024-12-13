import re

import numpy as np


def parse_input():
    with open("13.txt", "r") as file:
        data = file.read()
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    return [list(map(int, x)) for x in re.findall(pattern, data)]


MACHINES = parse_input()


def calc_tokens(ax, ay, bx, by, px, py):
    A = np.array([[ax, bx], [ay, by]])
    p = np.array([px, py])
    x = np.linalg.solve(A, p).round()
    return int(x @ (3, 1)) if all(A @ x == p) else 0


def part_one():
    return sum(calc_tokens(*machine) for machine in MACHINES)


def part_two():
    return sum(
        calc_tokens(
            *machine[:4], machine[4] + 10000000000000, machine[5] + 10000000000000
        )
        for machine in MACHINES
    )


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
