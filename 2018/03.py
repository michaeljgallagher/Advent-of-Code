import re


def parse_input():
    with open("03.txt", "r") as file:
        data = file.read()
    return [
        tuple(map(int, claim))
        for claim in re.findall(r"\d+ @ (\d+),(\d+): (\d+)x(\d+)", data)
    ]


CLAIMS = parse_input()
FABRIC = [[0] * 1000 for _ in range(1000)]


def part_one():
    for y, x, h, w in CLAIMS:
        for i in range(y, y + h):
            for j in range(x, x + w):
                FABRIC[i][j] += 1
    return sum(x > 1 for row in FABRIC for x in row)


def part_two():
    for id, (y, x, h, w) in enumerate(CLAIMS, start=1):
        if all(FABRIC[i][j] == 1 for i in range(y, y + h) for j in range(x, x + w)):
            return id


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
