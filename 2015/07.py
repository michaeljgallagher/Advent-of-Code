from functools import cache
from operator import and_, lshift, or_, rshift

with open("07.txt", "r") as file:
    raw_data = file.read().strip().split("\n")


def parse_input(raw_data):
    return {(s := line.split(" -> "))[1]: s[0].split(" ") for line in raw_data}


data = parse_input(raw_data)

OPS = {
    "AND": and_,
    "OR": or_,
    "RSHIFT": rshift,
    "LSHIFT": lshift,
}


@cache
def dp(wire):
    if wire.isdigit():
        return int(wire)
    left = data[wire]
    if len(left) == 1:
        return dp(left[0])
    elif len(left) == 2:
        return ~dp(left[1]) & 0xFFFF
    return OPS[left[1]](dp(left[0]), dp(left[2]))


def part_one():
    res = dp("a")
    dp.cache_clear()
    return res


def part_two():
    data["b"] = ["3176"]
    res = dp("a")
    dp.cache_clear()
    return res


print(f"Part 1: {part_one()}")  # 3176
print(f"Part 2: {part_two()}")  # 14710
