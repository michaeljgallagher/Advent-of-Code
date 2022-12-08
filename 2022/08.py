with open("08.txt", "r") as file:
    data = file.read().strip()

TREES = [list(map(int, line)) for line in data.split("\n")]
N, M = len(TREES), len(TREES[0])


def is_visible(i, j):
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj
        while (
            0 <= ni < N
            and 0 <= nj < M
            and TREES[ni][nj] < TREES[i][j]
        ):
            ni += di
            nj += dj
        if not (0 <= ni < N and 0 <= nj < M):
            return True
    return False


def scenic_score(i, j):
    if (i, j) in ((0, 0), (0, M - 1), (N - 1, 0), (N - 1, M - 1)):
        return 0
    res = 1
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj
        cur = 0
        while 0 <= ni < N and 0 <= nj < M:
            cur += 1
            if TREES[ni][nj] >= TREES[i][j]:
                break
            ni += di
            nj += dj
        res *= cur
    return res


def part_one():
    return sum(is_visible(i, j) for i in range(N) for j in range(M))


def part_two():
    return max(scenic_score(i, j) for i in range(N) for j in range(M))


print(f"Part 1: {part_one()}")  # 1832
print(f"Part 2: {part_two()}")  # 157320
