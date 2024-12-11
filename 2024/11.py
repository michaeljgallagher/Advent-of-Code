import re
from functools import cache


def parse_input():
    with open("11.txt", "r") as file:
        data = file.read()
    return list(map(int, re.findall(r"(\d+)", data)))


STONES = parse_input()


@cache
def dp(x, n):
    if n == 0:
        return 1
    if x == 0:
        return dp(1, n - 1)
    if (sz := len(str(x))) & 1 == 0:
        return dp(int(str(x)[: sz >> 1]), n - 1) + dp(int(str(x)[sz >> 1 :]), n - 1)
    return dp(x * 2024, n - 1)


def part_one():
    return sum(dp(x, 25) for x in STONES)


def part_two():
    return sum(dp(x, 75) for x in STONES)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
