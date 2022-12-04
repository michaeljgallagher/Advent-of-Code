import re

with open("04.txt", "r") as file:
    data = file.read().strip()

PAIRS = [
    (
        set(range(int(a), int(b) + 1)),
        set(range(int(c), int(d) + 1)),
    )
    for a, b, c, d in re.findall(
        r"(\d+)-(\d+),(\d+)-(\d+)", data
    )
]


def part_one():
    return sum(len(x | y) == max(len(x), len(y)) for x, y in PAIRS)


def part_two():
    return sum(len(x & y) > 0 for x, y in PAIRS)


print(f"Part 1: {part_one()}")  # 567
print(f"Part 2: {part_two()}")  # 907
