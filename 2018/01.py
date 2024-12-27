from itertools import accumulate, cycle


def parse_input():
    with open("01.txt", "r") as file:
        data = file.read()
    return [int(x) for x in data.splitlines()]


SEQ = parse_input()


def part_one():
    return sum(SEQ)


def part_two():
    seen = set()
    for x in accumulate(cycle(SEQ)):
        if x in seen:
            return x
        seen.add(x)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
