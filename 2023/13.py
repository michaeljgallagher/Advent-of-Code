with open("13.txt", "r") as file:
    data = file.read().strip()

GRIDS = [x.split("\n") for x in data.split("\n\n")]


def find_line(grid, target):
    for i in range(1, len(grid)):
        cur = 0
        for a, b in zip(reversed(grid[:i]), grid[i:]):
            cur += sum(x != y for x, y in zip(a, b))
        if cur == target:
            return i
    return 0


def solve(target):
    return sum(
        find_line(tuple(zip(*grid)), target) + 100 * find_line(grid, target)
        for grid in GRIDS
    )


print(f"Part 1: {solve(0)}")  # 35210
print(f"Part 2: {solve(1)}")  # 31974
