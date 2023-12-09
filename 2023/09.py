from itertools import pairwise

with open("09.txt", "r") as file:
    data = file.read().strip()

ROWS = [[int(x) for x in row.split(" ")] for row in data.split("\n")]


def solve(row):
    if len(set(row)) == 1:
        return row[0]
    return row[-1] + solve([b - a for a, b in pairwise(row)])


def part_one():
    return sum(solve(row) for row in ROWS)


def part_two():
    return sum(solve(row[::-1]) for row in ROWS)


print(f"Part 1: {part_one()}")  # 1743490457
print(f"Part 2: {part_two()}")  # 1053
