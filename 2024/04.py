from itertools import product

with open("04.txt", "r") as file:
    data = file.read().strip()

GRID = data.splitlines()
N, M = len(GRID), len(GRID[0])


def search_xmas(i, j):
    res = 0
    for di, dj in filter(any, product(range(-1, 2), repeat=2)):
        ni, nj = i, j
        xmas = 1
        for c in "MAS":
            ni += di
            nj += dj
            if 0 > ni or ni >= N or 0 > nj or nj >= M or GRID[ni][nj] != c:
                xmas = 0
                break
        res += xmas
    return res


def search_x_mas(i, j):
    return (
        1 <= i < N - 1
        and 1 <= j < M - 1
        and GRID[i - 1][j - 1] + GRID[i][j] + GRID[i + 1][j + 1] in ("MAS", "SAM")
        and GRID[i - 1][j + 1] + GRID[i][j] + GRID[i + 1][j - 1] in ("MAS", "SAM")
    )


def part_one():
    return sum(
        search_xmas(i, j) for i in range(N) for j in range(M) if GRID[i][j] == "X"
    )


def part_two():
    return sum(
        search_x_mas(i, j) for i in range(N) for j in range(M) if GRID[i][j] == "A"
    )


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
