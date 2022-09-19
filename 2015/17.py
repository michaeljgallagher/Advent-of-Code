import re

with open("17.txt", "r") as file:
    data = file.read()

NUMS = tuple(map(int, re.findall(r"(\d+)", data)))


def recur(bins, rem, used=0):
    if rem == 0:
        res.append(used)
    if rem > 0 and bins:
        recur(bins[1:], rem, used)
        recur(bins[1:], rem - bins[0], used + 1)


res = []
recur(NUMS, 150)


def part_one():
    return len(res)


def part_two():
    lo = min(res)
    return sum(x == lo for x in res)


print(f"Part 1: {part_one()}")  # 1304
print(f"Part 2: {part_two()}")  # 18
