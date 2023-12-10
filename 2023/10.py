with open("10.txt", "r") as file:
    data = file.read().strip()

GRID = data.split("\n")
MOVES = {
    ("|", (1, 0)): (1, 0),
    ("|", (-1, 0)): (-1, 0),
    ("-", (0, 1)): (0, 1),
    ("-", (0, -1)): (0, -1),
    ("L", (0, -1)): (-1, 0),
    ("L", (1, 0)): (0, 1),
    ("J", (0, 1)): (-1, 0),
    ("J", (1, 0)): (0, -1),
    ("7", (0, 1)): (1, 0),
    ("7", (-1, 0)): (0, -1),
    ("F", (0, -1)): (1, 0),
    ("F", (-1, 0)): (0, 1),
}
START = next(
    (i, j) for i, row in enumerate(GRID) for j, v in enumerate(row) if v == "S"
)


def find_start_orientation(start):
    n, m = len(GRID), len(GRID[0])
    i, j = start
    dirs = [(-1, 0, "|7F"), (1, 0, "|LJ"), (0, -1, "-FL"), (0, 1, "-J7")]
    for di, dj, valid in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and GRID[ni][nj] in valid:
            return "|" if di else "-", (di, dj)


def find_path():
    cur, dir = find_start_orientation(START)
    i, j = START
    res = [(i, j)]
    while True:
        dir = MOVES[(cur, dir)]
        di, dj = dir
        i, j = i + di, j + dj
        if (i, j) == START:
            break
        cur = GRID[i][j]
        res.append((i, j))
    return res


def shoelace_area(points):
    n = len(points)
    res = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        res += x1 * y2 - x2 * y1
    return abs(res) >> 1


def part_one():
    return len(find_path()) >> 1


def part_two():
    return shoelace_area(find_path()) - part_one() + 1


print(f"Part 1: {part_one()}")  # 6757
print(f"Part 2: {part_two()}")  # 523
