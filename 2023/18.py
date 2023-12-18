import re

with open("18.txt", "r") as file:
    data = file.read().strip()

PLAN = [(d, int(n), color) for d, n, color in re.findall(r"(\w) (\d+) \(#(.+)\)", data)]


def shoelace_area(points):
    n = len(points)
    res = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        res += x1 * y2 - x2 * y1
    return abs(res) >> 1


def solve(pt2=False):
    dirs = (
        [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if pt2
        else {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
    )
    i, j = 0, 0
    points = []
    perim = 0
    for d, n, color in PLAN:
        if pt2:
            n, d = int(color[:5], 16), int(color[-1])
        perim += n
        di, dj = dirs[d]
        i += n * di
        j += n * dj
        points.append((i, j))
    return shoelace_area(points) + (perim >> 1) + 1


print(f"Part 1: {solve()}")  # 47675
print(f"Part 2: {solve(True)}")  # 122103860427465
