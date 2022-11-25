import re
from collections import defaultdict

with open("10.txt", "r") as file:
    data = file.read().strip()

VALS = re.compile(r"value (\d+) goes to bot (\d+)")
GIVES = re.compile(
    r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)"
)


def setup(data):
    bots = defaultdict(list)
    commands = defaultdict(list)
    outs = {}
    stack = []
    for line in data.split("\n"):
        if m := VALS.match(line):
            bots[int(m.group(2))].append(int(m.group(1)))
            if len(bots[int(m.group(2))]) == 2:
                stack.append(int(m.group(2)))
        elif m := GIVES.match(line):
            commands[int(m.group(1))] = (
                m.group(2),
                int(m.group(3)),
                m.group(4),
                int(m.group(5)),
            )
    return bots, commands, outs, stack


def step(bots, commands, outs, stack):
    bot = stack.pop()
    lo, hi = min(bots[bot]), max(bots[bot])
    lo_bo, lo_b, hi_bo, hi_b = commands[bot]
    if lo_bo == "bot":
        bots[lo_b].append(lo)
        if len(bots[lo_b]) == 2:
            stack.append(lo_b)
    else:
        outs[lo_b] = lo
    if hi_bo == "bot":
        bots[hi_b].append(hi)
        if len(bots[hi_b]) == 2:
            stack.append(hi_b)
    else:
        outs[hi_b] = hi


def part_one():
    bots, commands, outs, stack = setup(data)
    while stack:
        if set(bots[stack[-1]]) == {17, 61}:
            return stack[-1]
        step(bots, commands, outs, stack)


def part_two():
    bots, commands, outs, stack = setup(data)
    while stack:
        step(bots, commands, outs, stack)
    return outs[0] * outs[1] * outs[2]


print(f"Part 1: {part_one()}")  # 93
print(f"Part 2: {part_two()}")  # 47101
