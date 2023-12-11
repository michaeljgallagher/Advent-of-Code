with open("11.txt", "r") as file:
    data = file.read().strip()

GRID = data.split("\n")


def dist(u, v):
    return sum(abs(x - y) for x, y in zip(u, v))


def locate_galaxies(grid, expand=2):
    empty_rows = {i for i, row in enumerate(grid) if all(c == "." for c in row)}
    empty_cols = {j for j, col in enumerate(zip(*grid)) if all(c == "." for c in col)}
    galaxies = []
    di = 0
    for i, row in enumerate(grid):
        if i in empty_rows:
            di += expand - 1
        dj = 0
        for j, c in enumerate(row):
            if j in empty_cols:
                dj += expand - 1
            if c == "#":
                galaxies.append((i + di, j + dj))
    return galaxies


def solve(pt2=False):
    galaxies = locate_galaxies(GRID, expand=1000000 if pt2 else 2)
    return sum(
        dist(u, v) for i, u in enumerate(galaxies[:-1]) for v in galaxies[i + 1 :]
    )


print(f"Part 1: {solve()}")  # 9799681
print(f"Part 2: {solve(True)}")  # 513171773355
