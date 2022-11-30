import re
from itertools import count

with open("13.txt", "r") as file:
    data = file.read().strip()

LAYERS = {
    int(k): int(v)
    for line in data.splitlines()
    for k, v in [line.split(": ")]
}


def part_one():
    res = 0
    for i in range(max(LAYERS) + 1):
        if i in LAYERS:
            if i % (LAYERS[i] * 2 - 2) == 0:
                res += i * LAYERS[i]
    return res


def part_two():
    for t in count():
        if all((i + t) % (LAYERS[i] * 2 - 2) for i in LAYERS):
            return t


print(f"Part 1: {part_one()}")  # 2604
print(f"Part 2: {part_two()}")  # 3941460
