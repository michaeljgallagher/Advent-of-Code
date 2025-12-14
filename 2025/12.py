from math import prod


def parse_input():
    with open("12.txt", "r") as f:
        data = f.read()
    *a, b = data.split("\n\n")
    presents = [x.count("#") for x in a]
    regions = [
        (prod(map(int, dims.split("x"))), list(map(int, nums.split())))
        for dims, nums in (line.split(": ") for line in b.splitlines())
    ]
    return presents, regions


def part_one():
    presents, regions = parse_input()
    return sum(
        area >= sum(presents[i] * v for i, v in enumerate(gifts))
        for area, gifts in regions
    )


print(f"Part 1: {part_one()}")
