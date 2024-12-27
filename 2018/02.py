from collections import Counter
from itertools import chain


def parse_input():
    with open("02.txt", "r") as file:
        data = file.read()
    return data.splitlines()


BOXES = parse_input()


def part_one():
    freq = Counter(chain.from_iterable(set(Counter(box).values()) for box in BOXES))
    return freq[2] * freq[3]


def part_two():
    for a in BOXES:
        for b in BOXES:
            cur = "".join(c for c, d in zip(a, b) if c == d)
            if len(cur) == 25:
                return cur


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
