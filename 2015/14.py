import re

with open("14.txt", "r") as file:
    data = file.read().strip().split("\n")


def parse_input(data):
    return [tuple(map(int, re.findall(r"(\d+)", line))) for line in data]


def calc_dist(velo, time, rest, elapsed):
    n, rm = divmod(elapsed, time + rest)
    res = (n * time + min(time, rm)) * velo
    return res


def part_one():
    reindeer = parse_input(data)
    return max(calc_dist(*rd, 2503) for rd in reindeer)


def part_two():
    reindeer = parse_input(data)
    scores = [0] * len(reindeer)
    for i in range(1, 2504):
        cur = [calc_dist(*rd, i) for rd in reindeer]
        high = max(cur)
        for i, v in enumerate(cur):
            scores[i] += high == v
    return max(scores)


print(f"Part 1: {part_one()}")  # 2660
print(f"Part 2: {part_two()}")  # 1256
