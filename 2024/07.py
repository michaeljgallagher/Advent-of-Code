import re
from functools import reduce
from itertools import product
from operator import add, mul


def parse_input():
    with open("07.txt", "r") as file:
        data = file.read()
    eqs = [tuple(map(int, re.findall(r"(\d+)", row))) for row in data.splitlines()]
    return eqs


EQS = parse_input()


def check_eq(eq, operators):
    test_val, nums = eq[0], eq[1:]
    for ops in product(operators, repeat=(len(nums) - 1)):
        if (
            reduce(lambda acc, x: x[0](acc, x[1]), zip(ops, nums[1:]), nums[0])
            == test_val
        ):
            return True
    return False


def part_one():
    return sum(eq[0] for eq in EQS if check_eq(eq, (add, mul)))


def part_two():
    def concat(a, b):
        a *= 10 ** len(str(b))
        return a + b

    return sum(eq[0] for eq in EQS if check_eq(eq, (add, mul, concat)))


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
