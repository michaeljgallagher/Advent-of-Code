import re
from collections import defaultdict

with open("19.txt", "r") as file:
    data = file.read().strip()

MOLECULE = data.split("\n")[-1]
REPLACEMENTS = defaultdict(list)

for k, v in re.findall(r"(\w+) => (\w+)", data):
    REPLACEMENTS[k].append(v)


def part_one():
    res = set()
    for k, vals in REPLACEMENTS.items():
        n = len(k)
        i = MOLECULE.find(k)
        while i != -1:
            for v in vals:
                res.add(MOLECULE[:i] + v + MOLECULE[i + n :])
            i = MOLECULE.find(k, i + n)
    return len(res)


def part_two():
    elements = sum(c.isupper() for c in MOLECULE)
    a, b = MOLECULE.count("Rn"), MOLECULE.count("Y")
    return elements - 2 * (a + b) - 1


print(f"Part 1: {part_one()}")  # 509
print(f"Part 2: {part_two()}")  # 195
