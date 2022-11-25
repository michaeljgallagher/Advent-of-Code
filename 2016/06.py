from collections import Counter

with open("06.txt", "r") as file:
    data = file.read().strip()

MESSAGES = data.split("\n")


def solve(least_common=False):
    return "".join(
        count.most_common()[0 - least_common][0]
        for count in [Counter(message) for message in zip(*MESSAGES)]
    )


print(f"Part 1: {solve()}")  # dzqckwsd
print(f"Part 2: {solve(least_common=True)}")  # lragovly
