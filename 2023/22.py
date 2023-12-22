from collections import defaultdict

with open("22.txt", "r") as file:
    data = file.read().strip()


def get_bricks(data):
    bricks = [
        list(map(list, zip(*(map(int, pair.split(",")) for pair in row.split("~")))))
        for row in data.split("\n")
    ]
    return sorted(bricks, key=lambda x: x[2])


def drop_bricks(bricks):
    heights = defaultdict(lambda: (-1, 0))
    supports = {}
    for i, brick in enumerate(bricks):
        cur = -1
        touching = set()
        (xl, xr), (yl, yr), (zl, zr) = brick
        for x in range(xl, xr + 1):
            for y in range(yl, yr + 1):
                idx, height = heights[x, y]
                if height + 1 > cur:
                    cur = height + 1
                    touching = {idx}
                elif height + 1 == cur:
                    touching.add(idx)
        if drop := zl - cur:
            brick[2][0] -= drop
            brick[2][1] -= drop
        for x in range(xl, xr + 1):
            for y in range(yl, yr + 1):
                heights[x, y] = (i, brick[2][1])
        supports[i] = touching
    return supports


def reachable(g, start):
    indeg = [0] * len(g)
    for vs in g:
        for v in vs:
            indeg[v] += 1
    res = 0
    q = [start]
    while q:
        res += 1
        u = q.pop()
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return res - 1


def part_one():
    bricks = get_bricks(data)
    supports = drop_bricks(bricks)
    res = set()
    for touching in supports.values():
        if len(touching) == 1 and (idx := next(iter(touching))) != -1:
            res.add(idx)
    return len(bricks) - len(res)


def part_two():
    bricks = get_bricks(data)
    supports = drop_bricks(bricks)
    g = [[] for _ in bricks]
    for i, touching in supports.items():
        for u in touching:
            if u != -1:
                g[u].append(i)
    return sum(reachable(g, i) for i in range(len(bricks)))


print(f"Part 1: {part_one()}")  # 416
print(f"Part 2: {part_two()}")  # 60963
