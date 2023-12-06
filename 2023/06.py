import re
from math import prod

with open("06.txt", "r") as file:
    data = file.read().strip()

RACES = list(zip(*(map(int, re.findall(r"(\d+)", x)) for x in data.split("\n"))))


def is_winner(hold, time, dist):
    return hold * (time - hold) > dist


def bsl(time, dist):
    lo, hi = 0, time
    while lo < hi:
        mid = lo + (hi - lo >> 1)
        if is_winner(mid, time, dist):
            hi = mid
        else:
            lo = mid + 1
    return lo


def bsr(time, dist):
    lo, hi = 0, time
    while lo <= hi:
        mid = lo + (hi - lo >> 1)
        if is_winner(mid, time, dist):
            lo = mid + 1
        else:
            hi = mid - 1
    return hi


def num_winners(time, dist):
    return bsr(time, dist) - bsl(time, dist) + 1


def part_one():
    return prod(num_winners(t, d) for t, d in RACES)


def part_two():
    t, d = (int("".join(str(x) for x in race)) for race in zip(*RACES))
    return num_winners(t, d)


print(f"Part 1: {part_one()}")  # 140220
print(f"Part 2: {part_two()}")  # 39570185
