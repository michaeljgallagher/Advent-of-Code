import re
from itertools import batched
from math import prod

with open("19.txt", "r") as file:
    A, B = file.read().strip().split("\n\n")

PARTS = [
    {
        k: int(v)
        for k, v in batched(
            *re.findall(r"(x)=(\d+),(m)=(\d+),(a)=(\d+),(s)=(\d+)", row), n=2
        )
    }
    for row in B.split("\n")
]
WORKFLOWS = {
    k: v for row in A.split("\n") for k, v in re.findall(r"(\w+)\{(.+)\}", row)
}


def solve_one(name, workflows, part):
    if name == "A":
        return True
    elif name == "R":
        return False
    rules = workflows[name].split(",")
    for rule in rules:
        if len(w := rule.split(":")) == 1:
            return solve_one(w.pop(), workflows, part)
        check, nxt = w
        cat, symb, n = check[0], check[1], int(check[2:])
        if (symb == ">" and part[cat] > n) or (symb == "<" and part[cat] < n):
            return solve_one(nxt, workflows, part)


def solve_two(name, workflows, ranges):
    if name == "A":
        return prod(len(x) for x in ranges.values())
    if name == "R":
        return 0
    res = 0
    left = {k: set(v) for k, v in ranges.items()}
    rules = workflows[name].split(",")
    for rule in rules:
        if len(w := rule.split(":")) == 1:
            res += solve_two(w.pop(), workflows, left)
            break
        check, nxt = w
        cat, symb, n = check[0], check[1], int(check[2:])
        possible = set(range(n + 1, 4001)) if symb == ">" else set(range(1, n))
        nranges = {}
        for k, v in left.items():
            if k == cat:
                nranges[k] = possible & v
                v -= nranges[k]
            else:
                nranges[k] = v
        res += solve_two(nxt, workflows, nranges)
    return res


def part_one():
    return sum(sum(r.values()) for r in PARTS if solve_one("in", WORKFLOWS, r))


def part_two():
    return solve_two(
        "in",
        WORKFLOWS,
        {
            "x": set(range(1, 4001)),
            "m": set(range(1, 4001)),
            "a": set(range(1, 4001)),
            "s": set(range(1, 4001)),
        },
    )


print(f"Part 1: {part_one()}")  # 391132
print(f"Part 2: {part_two()}")  # 128163929109524
