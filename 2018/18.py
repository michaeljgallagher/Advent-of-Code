from itertools import count, product


def parse_input():
    with open("18.txt", "r") as file:
        data = file.read()
    return list(map(list, data.strip().splitlines()))


N, M = 50, 50


def check_neis(grid, i, j):
    trees = yard = 0
    for di, dj in filter(any, product((-1, 0, 1), repeat=2)):
        ni, nj = i + di, j + dj
        if not (0 <= ni < N and 0 <= nj < M):
            continue
        if grid[ni][nj] == "|":
            trees += 1
        elif grid[ni][nj] == "#":
            yard += 1
    return trees, yard


def change_acre(grid, i, j):
    trees, yard = check_neis(grid, i, j)
    match grid[i][j]:
        case ".":
            return "|" if trees >= 3 else "."
        case "|":
            return "#" if yard >= 3 else "|"
        case "#":
            return "#" if yard > 0 and trees > 0 else "."


def step(grid):
    res = [[None] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            res[i][j] = change_acre(grid, i, j)
    return res


def calc(grid):
    trees = yard = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "|":
                trees += 1
            if grid[i][j] == "#":
                yard += 1
    return trees * yard


def part_one():
    grid = parse_input()
    for _ in range(10):
        grid = step(grid)
    return calc(grid)


def part_two():
    grid = parse_input()
    seen = {}
    vals = []
    for i in count():
        state = tuple("".join(row) for row in grid)
        if state in seen:
            start = seen[state]
            cycle_length = i - start
            return vals[start + (1000000000 - start) % cycle_length]
        cur = calc(grid)
        seen[state] = i
        vals.append(cur)
        grid = step(grid)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
