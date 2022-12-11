import re
from collections import deque
from math import prod
from operator import add, mul


def parse_monkey(s):
    items = deque(
        int(x)
        for x in re.search(r"Starting items: (\d+(,\s*\d+)*)", s)
        .group(1)
        .split(", ")
    )
    op, fac = re.findall(r"new = old (.+)", s)[0].split()
    op = {"+": add, "*": mul}[op]
    fac = int(fac) if fac.isdigit() else fac
    test = int(re.findall(r"divisible by (\d+)", s)[0])
    true = int(re.findall(r"true: throw to monkey (\d+)", s)[0])
    false = int(re.findall(r"false: throw to monkey (\d+)", s)[0])
    return items, op, fac, test, true, false


def process_monkey(monkeys, i, part_one=True):
    items, op, fac, test, true, false = monkeys[i]
    lcm = prod(monkey[3] for monkey in monkeys)
    while items:
        item = items.popleft()
        item = op(item, item if fac == "old" else fac)
        if part_one:
            item //= 3
        item %= lcm
        if item % test == 0:
            monkeys[true][0].append(item)
        else:
            monkeys[false][0].append(item)
    return monkeys


def process_round(monkeys, part_one=True):
    inspections = []
    for i in range(len(monkeys)):
        inspections.append(len(monkeys[i][0]))
        monkeys = process_monkey(monkeys, i, part_one)
    return monkeys, inspections


def solve(data, part_one=True, rounds=20):
    monkeys = [parse_monkey(m) for m in data.split("\n\n")]
    inspections = [0] * len(monkeys)
    for _ in range(rounds):
        monkeys, new_ins = process_round(monkeys, part_one)
        inspections = [a + b for a, b in zip(inspections, new_ins)]
    return prod(sorted(inspections)[-2:])


with open("11.txt", "r") as file:
    data = file.read().strip()

print(f"Part 1: {solve(data)}")  # 182293
print(f"Part 2: {solve(data, part_one=False, rounds=10000)}")  # 54832778815
