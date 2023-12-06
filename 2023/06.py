import re
from math import prod

with open("06.txt", "r") as file:
    data = file.read().strip()

RACES = list(zip(*(map(int, re.findall(r"(\d+)", x)) for x in data.split("\n"))))


def binary_search(time, dist, left=True):
    lo, hi = 0, time
    while lo <= hi:
        mid = lo + (hi - lo >> 1)
        if mid * (time - mid) > dist:
            if left:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if left:
                lo = mid + 1
            else:
                hi = mid - 1
    return lo if left else hi


def num_winners(time, dist):
    return binary_search(time, dist, False) - binary_search(time, dist) + 1


def part_one():
    return prod(num_winners(t, d) for t, d in RACES)


def part_two():
    return num_winners(*(int("".join(str(x) for x in race)) for race in zip(*RACES)))


print(f"Part 1: {part_one()}")  # 140220
print(f"Part 2: {part_two()}")  # 39570185
