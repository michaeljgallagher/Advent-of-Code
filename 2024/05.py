import re
from functools import cmp_to_key
from itertools import pairwise


def parse_input():
    with open("05.txt", "r") as file:
        data = file.read()
    rules_raw, pages_raw = data.strip().split("\n\n")
    rules = {(int(x), int(y)) for x, y in re.findall(r"(\d+)\|(\d+)", rules_raw)}
    pages = [[int(x) for x in line.split(",")] for line in pages_raw.splitlines()]
    return rules, pages


RULES, PAGES = parse_input()


def part_one():
    return sum(
        page[len(page) >> 1]
        for page in PAGES
        if all(pair in RULES for pair in pairwise(page))
    )


def part_two():
    unsorted = filter(
        lambda page: any(pair not in RULES for pair in pairwise(page)), PAGES
    )
    return sum(
        sorted(page, key=cmp_to_key(lambda x, y: -1 if (x, y) in RULES else 1))[
            len(page) >> 1
        ]
        for page in unsorted
    )


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
