import math
import re
from functools import cache
from itertools import batched, count


def parse_input():
    with open("10.txt", "r") as file:
        data = file.read()
    return list(batched(map(int, re.findall(r"-?\d+", data)), 4))


POINTS = parse_input()


@cache
def solve():
    space = math.inf
    prev = set()
    max_i = max_j = -math.inf
    min_i = min_j = math.inf
    for t in count():
        nmax_i = nmax_j = -math.inf
        nmin_i = nmin_j = math.inf
        cur = set()
        for j, i, dj, di in POINTS:
            i += di * t
            j += dj * t
            nmax_i = max(nmax_i, i)
            nmax_j = max(nmax_j, j)
            nmin_i = min(nmin_i, i)
            nmin_j = min(nmin_j, j)
            cur.add((i, j))
        nspace = nmax_i - nmin_i + nmax_j - nmin_j
        if nspace > space:
            return (
                "\n".join(
                    "".join(
                        "\u2588" if (x, y) in prev else " "
                        for y in range(min_j, max_j + 1)
                    )
                    for x in range(min_i, max_i + 1)
                ),
                t - 1,
            )
        else:
            space = nspace
            prev = cur
            max_i = nmax_i
            max_j = nmax_j
            min_i = nmin_i
            min_j = nmin_j


def part_one():
    return "\n" + solve()[0]


def part_two():
    return solve()[1]


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
