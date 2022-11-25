from itertools import accumulate


def solve(*args):
    return sum(2 * (x - 1) - 1 for x in accumulate(args))


print(f"Part 1: {solve(4, 2, 4)}")  # 31
print(f"Part 2: {solve(8, 2, 4)}")  # 55
