from collections import defaultdict
from itertools import combinations


def parse_input():
    with open("08.txt", "r") as file:
        data = file.read()
    grid = data.splitlines()
    antennas = defaultdict(list)
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v != ".":
                antennas[v].append((i, j))
    return antennas, len(grid), len(grid[0])


ANTENNAS, N, M = parse_input()


def calc_antinodes(u, v, pt2=False):
    ui, uj = u
    vi, vj = v
    di = ui - vi
    dj = uj - vj
    res = {(ui, uj), (vi, vj)} if pt2 else set()
    while 0 <= (ui := ui + di) < N and 0 <= (uj := uj + dj) < M:
        res |= {(ui, uj)}
        if not pt2:
            break
    while 0 <= (vi := vi - di) < N and 0 <= (vj := vj - dj) < M:
        res |= {(vi, vj)}
        if not pt2:
            break
    return res


def solve(pt2=False):
    return len(
        {
            antinode
            for locs in ANTENNAS.values()
            for u, v in combinations(locs, 2)
            for antinode in calc_antinodes(u, v, pt2)
        }
    )


def part_one():
    return solve()


def part_two():
    return solve(pt2=True)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
