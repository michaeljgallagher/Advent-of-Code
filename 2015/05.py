import re
from itertools import groupby

with open("05.txt", "r") as file:
    raw_data = file.read().strip()

data = raw_data.split("\n")


def is_nice(s):
    check1 = sum(c in "aeiou" for c in s) >= 3
    check2 = check3 = False
    for _, grp in groupby(s):
        if len(list(grp)) >= 2:
            check2 = True
            break
    check3 = len(re.findall(r"ab|cd|pq|xy", s)) == 0
    return check1 & check2 & check3


def is_nice_2(s):
    check1 = any(s[i : i + 2] in s[:i] for i in range(len(s) - 1))
    check2 = any(a == b for a, b in zip(s, s[2:]))
    return check1 & check2


def part_one(data):
    return sum(map(is_nice, data))


def part_two(data):
    return sum(map(is_nice_2, data))


print(f"Part 1: {part_one(data)}")  # 255
print(f"Part 2: {part_two(data)}")  # 55
