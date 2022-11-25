import re
from itertools import count

with open("15.txt", "r") as file:
    data = file.read().strip()

DISCS = [
    (int(num_pos), int(pos) + i)
    for i, (num_pos, pos) in enumerate(
        re.findall(r"(\d+) positions; .+ (\d+)", data), start=1
    )
]


def solve(discs):
    for t in count():
        if all((pos + t) % num_pos == 0 for num_pos, pos in discs):
            return t


print(f"Part 1: {solve(DISCS)}")  # 203660
print(f"Part 2: {solve(DISCS + [(11, 7)])}")  # 2408135
