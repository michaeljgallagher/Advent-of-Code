from itertools import permutations

with open("02.txt", "r") as file:
    data = file.read().strip()

SPREADSHEET = [
    list(map(int, line.split())) for line in data.splitlines()
]


def part_one():
    return sum(max(line) - min(line) for line in SPREADSHEET)


def part_two():
    return sum(
        a // b
        for row in SPREADSHEET
        for a, b in permutations(row, 2)
        if a % b == 0
    )


print(f"Part 1: {part_one()}")  # 47623
print(f"Part 2: {part_two()}")  # 312
