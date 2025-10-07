import heapq
import re
from math import inf


def parse_input():
    with open("23.txt", "r") as file:
        data = file.read()
    res = []
    for x, y, z, r in re.findall(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(-?\d+)", data):
        res.append((int(r), int(x), int(y), int(z)))
    return sorted(res, reverse=True)


NANOBOTS = parse_input()


def part_one():
    def manhattan(u, v):
        return sum(abs(a - b) for a, b in zip(u, v))

    R, X, Y, Z = NANOBOTS[0]
    return sum(manhattan((X, Y, Z), (x, y, z)) <= R for _, x, y, z in NANOBOTS)


def part_two():
    def num_in_range(x, y, z, sz):
        res = 0
        for r, xx, yy, zz in NANOBOTS:
            cur = 0
            cur += max(0, x - xx, xx - (x + sz))
            cur += max(0, y - yy, yy - (y + sz))
            cur += max(0, z - zz, zz - (z + sz))
            if cur <= r:
                res += 1
        return res

    lo = min(min(x, y, z) for _, x, y, z in NANOBOTS)
    hi = max(max(x, y, z) for _, x, y, z in NANOBOTS)
    sz = 1
    while sz < hi - lo:
        sz <<= 1
    start = num_in_range(lo, lo, lo, sz)
    heap = [(-start, lo, lo, lo, sz)]
    cnt = 0
    res = inf
    while heap:
        cur, x, y, z, sz = heapq.heappop(heap)
        cur = -cur
        if sz == 0:
            d = abs(x) + abs(y) + abs(z)
            if cur > cnt or (cur == cnt and d < res):
                cnt = cur
                res = d
            continue
        if cur < cnt:
            continue
        nsz = sz >> 1
        for dx in (0, nsz):
            for dy in (0, nsz):
                for dz in (0, nsz):
                    nx, ny, nz = x + dx, y + dy, z + dz
                    nxt = num_in_range(nx, ny, nz, nsz)
                    if nxt < cnt:
                        continue
                    heapq.heappush(heap, (-nxt, nx, ny, nz, nsz))
    return res


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
