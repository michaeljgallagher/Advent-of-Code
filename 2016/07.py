import re

with open("07.txt", "r") as file:
    data = file.read().strip()

IPS = [re.split(r"\[|\]", line) for line in data.split("\n")]
SUPER = [ip[::2] for ip in IPS]
HYPER = [ip[1::2] for ip in IPS]


def is_abba(s):
    return any(
        s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]
        for i in range(len(s) - 3)
    )


def is_ababab(sup, hyp):
    return any(
        a == c and a != b and b + a + b in hyp
        for a, b, c in zip(sup, sup[1:], sup[2:])
    )


def part_one():
    return sum(
        any(is_abba(s) for s in sup) and not any(is_abba(s) for s in hyp)
        for sup, hyp in zip(SUPER, HYPER)
    )


def part_two():
    return sum(
        any(is_ababab(sup, hyp) for sup in sups)
        for sups, hyps in zip(SUPER, HYPER)
        for hyp in hyps
    )


print(f"Part 1: {part_one()}")  # 118
print(f"Part 2: {part_two()}")  # 260
