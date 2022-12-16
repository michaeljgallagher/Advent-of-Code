import re

with open("15.txt", "r") as file:
    data = file.read().strip()


def manhattan(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


COORDS = [
    [int(d) for d in re.findall(r"-?\d+", line)]
    for line in data.splitlines()
]
DISTS = {(a, b): manhattan((a, b), (c, d)) for a, b, c, d in COORDS}


def part_one():
    res = set()
    for (sx, sy), dist in DISTS.items():
        ndist = abs(sy - 2000000)
        res.update(range(sx - dist + ndist, sx + dist - ndist))
    return len(res)


def part_two():
    A, B = set(), set()
    for (sx, sy), dist in DISTS.items():
        A.add(sy - sx + dist + 1)
        A.add(sy - sx - dist - 1)
        B.add(sx + sy + dist + 1)
        B.add(sx + sy - dist - 1)
    for a in A:
        for b in B:
            p, q = (b - a) // 2, (a + b) // 2
            if (
                0 < p < 4000000
                and 0 < q < 4000000
                and all(
                    DISTS[k] < manhattan((p, q), k)
                    for k in DISTS.keys()
                )
            ):
                return 4000000 * p + q


print(f"Part 1: {part_one()}")  # 5040643
print(f"Part 2: {part_two()}")  # 11016575214126
