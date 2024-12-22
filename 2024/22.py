from collections import defaultdict
from functools import reduce
from itertools import accumulate, pairwise


def parse_input():
    with open("22.txt", "r") as file:
        data = file.read()
    return list(map(int, data.splitlines()))


NUMS = parse_input()


def evolve(n):
    n = ((n << 6) ^ n) & 0xFFFFFF
    n = ((n >> 5) ^ n) & 0xFFFFFF
    n = ((n << 11) ^ n) & 0xFFFFFF
    return n


def part_one():
    return sum(reduce(lambda acc, _: evolve(acc), range(2000), n) for n in NUMS)


def part_two():
    freq = defaultdict(int)
    for n in NUMS:
        steps = list(accumulate(range(2000), lambda acc, _: evolve(acc), initial=n))
        delta = [y % 10 - x % 10 for x, y in pairwise(steps)]
        seen = set()
        for i in range(len(steps) - 4):
            cur = tuple(delta[i : i + 4])
            if cur in seen:
                continue
            seen.add(cur)
            freq[cur] += steps[i + 4] % 10
    return max(freq.values())


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
