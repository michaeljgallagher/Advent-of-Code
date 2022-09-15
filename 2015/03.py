from collections import defaultdict

with open("03.txt", "r") as file:
    raw_data = file.read().strip()

DIRS = {
    "^": 0 + 1j,
    ">": 1 + 0j,
    "v": 0 - 1j,
    "<": -1 - 0j,
}


def part_one(data):
    points = defaultdict(int)
    cur = 0 + 0j
    points[cur.real, cur.imag] += 1
    for c in data:
        cur += DIRS[c]
        points[cur.real, cur.imag] += 1
    return len(points)


def part_two(data):
    points = [defaultdict(int), defaultdict(int)]
    bots = [0 + 0j, 0 + 0j]
    i = 0
    cur = bots[i]
    cur_points = points[i]
    cur_points[cur.real, cur.imag] += 1
    for c in data:
        cur = bots[i]
        cur_points = points[i]
        cur += DIRS[c]
        bots[i] = cur
        cur_points[cur.real, cur.imag] += 1
        i = 1 - i
    a, b = points
    return len(set(a.keys()) | set(b.keys()))


print(f"Part 1: {part_one(raw_data)}")  # 2572
print(f"Part 2: {part_two(raw_data)}")  # 2631
