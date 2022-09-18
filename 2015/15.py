from math import prod
import re

with open("15.txt", "r") as file:
    data = file.read().strip().split("\n")


def parse_input(data):
    return [tuple(map(int, re.findall(r"(-?\d+)", line))) for line in data]


INGS = parse_input(data)


def partitions(n, r):
    if r == 1:
        yield (n,)
        return
    for i in range(n + 1):
        for j in partitions(n - i, r - 1):
            yield i, *j


def calc_score(p, ings):
    cur = []
    for i in range(len(ings)):
        x = sum(a[i] * b for a, b in zip(ings, p))
        cur.append(x if x > 0 else 0)
    return prod(cur)


def part_one():
    res = 0
    for p in partitions(100, len(INGS)):
        res = max(res, calc_score(p, INGS))
    return res


def part_two():
    res = 0
    for p in partitions(100, len(INGS)):
        if sum(a[4] * b for a, b in zip(INGS, p)) != 500:
            continue
        res = max(res, calc_score(p, INGS))
    return res


print(f"Part 1: {part_one()}")  # 222870
print(f"Part 2: {part_two()}")  # 117936
