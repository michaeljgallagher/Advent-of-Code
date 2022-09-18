import re
from collections import Counter

with open("16.txt", "r") as file:
    data = file.read().strip().split("\n")


def parse_line(s):
    return Counter({k: int(v) for k, v in re.findall(r"(\w+): (\d+)", s)})


def parse_input(data):
    return {i: parse_line(v) for i, v in enumerate(data, start=1)}


TAPE = parse_line(
    """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
)

SUES = parse_input(data)


def check_sue_1(i, tape, sues):
    sue = sues[i]
    check = Counter({k: tape[k] for k in tape.keys() & sue.keys()})
    return check == sue


def check_sue_2(i, tape, sues):
    sue = sues[i]
    same = Counter({k: tape[k] for k in tape.keys() & sue.keys()})
    check = (
        lambda k, v: v < sue[k]
        if k in ("cats", "trees")
        else v > sue[k]
        if k in ("pomeranians", "goldfish")
        else v == sue[k]
    )
    for k, v in same.items():
        if not check(k, v):
            return False
    return True


def part_one():
    for i in range(1, 501):
        if check_sue_1(i, TAPE, SUES):
            return i


def part_two():
    for i in range(1, 501):
        if check_sue_2(i, TAPE, SUES):
            return i


print(f"Part 1: {part_one()}")  # 373
print(f"Part 2: {part_two()}")  # 260
