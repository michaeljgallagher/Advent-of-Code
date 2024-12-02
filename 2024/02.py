from itertools import pairwise

with open("02.txt", "r") as file:
    data = file.read().strip().splitlines()


REPORTS = [[int(x) for x in row.split()] for row in data]


def check(report):
    a, b = report[:2]
    inc = (-1) ** (b < a)
    return all(1 <= inc * (b - a) <= 3 for a, b in pairwise(report))


def part_one():
    return sum(check(report) for report in REPORTS)


def part_two():
    return sum(
        any(check(report[:i] + report[i + 1 :]) for i in range(len(report)))
        for report in REPORTS
    )


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
