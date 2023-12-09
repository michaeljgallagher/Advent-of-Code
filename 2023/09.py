from itertools import pairwise

with open("09.txt", "r") as file:
    data = file.read().strip()

ROWS = [[int(x) for x in row.split(" ")] for row in data.split("\n")]


def solve(row):
    return row[-1] + (
        0 if len(set(row)) == 1 else solve([b - a for a, b in pairwise(row)])
    )


print(f"Part 1: {sum(solve(row) for row in ROWS)}")  # 1743490457
print(f"Part 2: {sum(solve(row[::-1]) for row in ROWS)}")  # 1053
