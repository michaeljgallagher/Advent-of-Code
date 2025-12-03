import re
from itertools import batched


def parse_input():
    with open("02.txt", "r") as f:
        data = f.read()
    return list(batched(map(int, re.findall(r"\d+", data)), 2))


def is_invalid(x, pt2=False):
    x = str(x)
    m = re.match(r"^(.*)\1+$", x)
    if m is None:
        return False
    return (pt2 and bool(m)) or (not pt2 and len(m.group(1)) << 1 == len(x))


def solve(pt2=False):
    return sum(
        x * is_invalid(x, pt2) for l, r in parse_input() for x in range(l, r + 1)
    )


print(f"Part 1: {solve()}")
print(f"Part 2: {solve(pt2=True)}")
