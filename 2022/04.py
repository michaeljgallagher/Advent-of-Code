import re

with open("04.txt", "r") as file:
    data = file.read().strip()

PAIRS = [
    tuple(map(int, g))
    for g in re.findall(
        r"(\d+)-(\d+),(\d+)-(\d+)", data
    )
]


def part_one():
    return sum(
        (a <= c and b >= d)
        or (a >= c and b <= d)
        for a, b, c, d in PAIRS
    )


def part_two():
    return sum(
        (a <= c and b >= c)
        or (a <= d and b >= d)
        or (c <= a and d >= a)
        or (c <= b and d >= b)
        for a, b, c, d in PAIRS
    )


print(f"Part 1: {part_one()}")  # 567
print(f"Part 2: {part_two()}")  # 907
