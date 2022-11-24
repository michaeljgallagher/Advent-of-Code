import re

with open("24.txt", "r") as file:
    data = file.read().strip()

PACKAGES = sorted(map(int, re.findall(r"(\d+)", data)), reverse=True)


def solve(num_groups=3):
    groups = set()
    target = sum(PACKAGES) // num_groups
    bound = len(PACKAGES) // num_groups

    def recur(weights, cur, qe, count):
        if cur == target:
            groups.add((count, qe))
            return
        if cur < target and weights and count < bound:
            recur(weights[1:], cur, qe, count)
            recur(weights[1:], cur + weights[0], qe * weights[0], count + 1)

    recur(PACKAGES, 0, 1, 0)
    return min(groups)[1]


print(f"Part 1: {solve(3)}")  # 11846773891
print(f"Part 2: {solve(4)}")  # 80393059
