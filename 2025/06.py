from functools import reduce
from itertools import pairwise
from operator import add, mul


def parse_input():
    with open("06.txt", "r") as f:
        data = f.read().splitlines()
    return data[:-1], data[-1]


NUMS, OPS = parse_input()


def part_one():
    return sum(
        reduce(op, col)
        for op, col in zip(
            [{"*": mul, "+": add}[x] for x in OPS.split()],
            zip(*(map(int, row.split()) for row in NUMS)),
        )
    )


def part_two():
    term = [i for i, v in enumerate(OPS) if v != " "] + [len(OPS) + 1]
    sliced = [[row[i : j - 1] for i, j in pairwise(term)] for row in NUMS]
    return sum(
        reduce(op, col)
        for op, col in zip(
            [{"*": mul, "+": add}[x] for x in OPS.split()],
            [[int("".join(c)) for c in zip(*col)] for col in zip(*sliced)],
        )
    )


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
