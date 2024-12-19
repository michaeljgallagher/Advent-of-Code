from functools import cache


def parse_input():
    with open("19.txt", "r") as file:
        data = file.read()
    patterns, designs = data.split("\n\n")
    return patterns.split(", "), designs.splitlines()


PATTERNS, DESIGNS = parse_input()


@cache
def possible(s, i=0, pt2=False):
    if i > len(s):
        return 0
    if i == len(s):
        return 1
    res = 0
    for pattern in PATTERNS:
        sz = len(pattern)
        if s[i : i + sz] == pattern:
            if pt2:
                res += possible(s, i + sz, pt2)
            else:
                res = res or possible(s, i + sz, pt2)
    return res


def part_one():
    return sum(map(possible, DESIGNS))


def part_two():
    return sum(possible(x, pt2=True) for x in DESIGNS)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
