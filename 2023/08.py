import re
from itertools import count
from math import lcm

with open("08.txt", "r") as file:
    data = file.read().strip()

INSTR, network = data.split("\n\n")
N = len(INSTR)
G = {
    a: (b, c)
    for line in network.split("\n")
    for a, b, c in [re.findall(r"(\w+)", line)]
}


def solve(u, *vs):
    for step in count():
        if u in vs:
            return step
        i = INSTR[step % N] == "R"
        u = G[u][i]


def part_one():
    return solve("AAA", "ZZZ")


def part_two():
    starts = [u for u in G if u[-1] == "A"]
    ends = [u for u in G if u[-1] == "Z"]
    return lcm(*(solve(u, *ends) for u in starts))


print(f"Part 1: {part_one()}")  # 18827
print(f"Part 2: {part_two()}")  # 20220305520997
