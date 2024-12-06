def parse_input():
    with open("06.txt", "r") as file:
        data = file.read()
    grid = data.splitlines()
    return grid


GRID = parse_input()
GUARD = next(
    (i, j) for i, row in enumerate(GRID) for j, c in enumerate(row) if c == "^"
)
N, M = len(GRID), len(GRID[0])


def check_new(ni, nj):
    i, j = GUARD
    di, dj = -1, 0
    seen = set()
    while 0 <= i < N and 0 <= j < M:
        if (i, j, di, dj) in seen:
            return True
        if (
            0 <= i + di < N
            and 0 <= j + dj < M
            and (GRID[i + di][j + dj] == "#" or (i + di, j + dj) == (ni, nj))
        ):
            di, dj = dj, -di
        else:
            seen.add((i, j, di, dj))
            i += di
            j += dj
    return False


def part_one():
    i, j = GUARD
    di, dj = -1, 0
    seen = set()
    while 0 <= i < N and 0 <= j < M:
        if 0 <= i + di < N and 0 <= j + dj < M and GRID[i + di][j + dj] == "#":
            di, dj = dj, -di
        else:
            seen.add((i, j))
            i += di
            j += dj
    return len(seen)


def part_two():
    return sum(check_new(i, j) for i in range(N) for j in range(M) if GRID[i][j] == ".")


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
