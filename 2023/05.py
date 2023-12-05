from itertools import batched

with open("05.txt", "r") as file:
    data = file.read().strip()

SEEDS = list(map(int, data.split("\n\n")[0].split(": ")[1].split()))
MAPS = [
    [list(map(int, y.split(" "))) for y in x.split("\n")[1:]]
    for x in data.split("\n\n")[1:]
]


def seed_location(cur, i=0):
    if i == len(MAPS):
        return cur
    for dst, src, offset in MAPS[i]:
        if src <= cur < src + offset:
            return seed_location(dst + cur - src, i + 1)
    return seed_location(cur, i + 1)


def part_one():
    return min(seed_location(seed) for seed in SEEDS)


def dfs_part_two(cur, i=0):
    if i == len(MAPS):
        return cur
    res = []
    ranges = cur
    for dst, src, offset in MAPS[i]:
        nranges = []
        for s, e in ranges:
            l = (s, min(e, src))
            m = (max(s, src), min(src + offset, e))
            r = (max(src + offset, s), e)
            if l[0] < l[1]:
                nranges.append(l)
            if m[0] < m[1]:
                res.append((dst + m[0] - src, dst + m[1] - src))
            if r[0] < r[1]:
                nranges.append(r)
        ranges = nranges
    return dfs_part_two(res + ranges, i + 1)


def part_two():
    return min(
        min(dfs_part_two([(start, start + offset)]))[0]
        for start, offset in batched(SEEDS, n=2)
    )


print(f"Part 1: {part_one()}")  # 379811651
print(f"Part 2: {part_two()}")  # 27992443
