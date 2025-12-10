import re
from itertools import combinations, pairwise


def parse_input():
    with open("09.txt", "r") as f:
        data = f.read()
    return [(int(x[0]), int(x[1])) for x in re.findall(r"(\d+),(\d+)", data)]


POINTS = parse_input()


def part_one():
    return max(
        (abs(ui - vi) + 1) * (abs(uj - vj) + 1)
        for (ui, uj), (vi, vj) in combinations(POINTS, 2)
    )


def part_two():
    def is_in(ui, uj, vi, vj):
        i_min, i_max = min(ui, vi), max(ui, vi)
        j_min, j_max = min(uj, vj), max(uj, vj)
        for (xi, xj), (yi, yj) in pairwise(POINTS + [POINTS[0]]):
            if xj == yj:
                if j_min < xj < j_max and (
                    min(xi, yi) <= i_min < max(xi, yi)
                    or min(xi, yi) < i_max <= max(xi, yi)
                ):
                    return False
            elif xi == yi:
                if i_min < xi < i_max and (
                    min(xj, yj) <= j_min < max(xj, yj)
                    or min(xj, yj) < j_max <= max(xj, yj)
                ):
                    return False
        return True

    return max(
        (abs(ui - vi) + 1) * (abs(uj - vj) + 1)
        for (ui, uj), (vi, vj) in combinations(POINTS, 2)
        if is_in(ui, uj, vi, vj)
    )


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
