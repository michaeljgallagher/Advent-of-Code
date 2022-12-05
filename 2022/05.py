import re

with open("05.txt", "r") as file:
    data = file.read().strip()

MOVES = [
    (int(x), int(y) - 1, int(z) - 1)
    for x, y, z in re.findall(
        r"move (\d+) from (\d+) to (\d+)", data
    )
]


def parse_crates(arrangement):
    stacks = [[] for _ in range(9)]
    for line in arrangement.split("\n"):
        for i, c in enumerate(line):
            if c.isalpha():
                stacks[i // 4].append(c)
    return [stack[::-1] for stack in stacks]


def solve(part_two=False):
    stacks = parse_crates(data.split("\n\n")[0])
    for n, i, j in MOVES:
        cur = [stacks[i].pop() for _ in range(n)]
        stacks[j].extend(cur[::-1] if part_two else cur)
    return "".join(stack[-1] for stack in stacks)


print(f"Part 1: {solve()}")  # QNHWJVJZW
print(f"Part 2: {solve(True)}")  # BPCZJLFJW
