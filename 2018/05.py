import math
from string import ascii_letters


def parse_input():
    with open("05.txt", "r") as file:
        data = file.read()
    return data.strip()


POLYMER = parse_input()


def solve(polymer):
    stack = []
    for c in polymer:
        if not stack or abs(ord(c) - ord(stack[-1])) != 32:
            stack.append(c)
        elif stack and abs(ord(c) - ord(stack[-1])) == 32:
            stack.pop()
    return len(stack)


def part_one():
    return solve(POLYMER)


def part_two():
    res = math.inf
    for lo, up in zip(ascii_letters[:26], ascii_letters[26:]):
        polymer = POLYMER.replace(lo, "").replace(up, "")
        res = min(res, solve(polymer))
    return res


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
