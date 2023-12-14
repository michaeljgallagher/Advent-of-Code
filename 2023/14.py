from itertools import count

with open("14.txt", "r") as file:
    data = file.read().strip()


def get_state(data):
    grid = [list(row) for row in data.split("\n")]
    rocks = [
        (i, j)
        for j in range(len(grid[0]))
        for i in range(len(grid))
        if grid[i][j] == "O"
    ]
    return rocks, grid


def tilt(i, j, di, dj, grid):
    n, m = len(grid), len(grid[0])
    grid[i][j] = "."
    if di == -1:
        while i > 0 and grid[i - 1][j] == ".":
            i -= 1
    elif di == 1:
        while i < n - 1 and grid[i + 1][j] == ".":
            i += 1
    elif dj == -1:
        while j > 0 and grid[i][j - 1] == ".":
            j -= 1
    else:
        while j < m - 1 and grid[i][j + 1] == ".":
            j += 1
    grid[i][j] = "O"
    return i, j


def calc_load(g):
    return sum(i * row.count("O") for i, row in enumerate(g[::-1], start=1))


def cycle(rocks, grid):
    keys = [
        lambda x: x[1],
        lambda x: -x[0],
        lambda x: -x[1],
        lambda x: x[0],
    ]
    for k, (di, dj) in enumerate(((-1, 0), (0, -1), (1, 0), (0, 1))):
        nrocks = []
        for i, j in rocks:
            ni, nj = tilt(i, j, di, dj, grid)
            nrocks.append((ni, nj))
        rocks = sorted(nrocks, key=keys[k])
    return rocks, grid


def find_cycle(rocks, grid):
    seen = {}
    for i in count(start=1):
        rocks, grid = cycle(rocks, grid)
        cur = "\n".join("".join(row) for row in grid)
        if cur in seen:
            return seen[cur], i - seen[cur], seen
        seen[cur] = i


def part_one():
    rocks, grid = get_state(data)
    for i, j in rocks:
        tilt(i, j, -1, 0, grid)
    return calc_load(grid)


def part_two():
    rocks, grid = get_state(data)
    start, length, seen = find_cycle(rocks, grid)
    rseen = {v: k for k, v in seen.items()}
    res = rseen[(start + (1000000000 - start) % length)]
    return calc_load(res.split("\n"))


print(f"Part 1: {part_one()}")  # 108935
print(f"Part 2: {part_two()}")  # 100876
