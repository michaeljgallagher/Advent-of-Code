from collections import deque

with open("09.txt", "r") as file:
    raw_data = file.read()


def parse_input(raw_data):
    res = []
    for line in raw_data.split("\n"):
        res.append(list(map(int, line)))
    return res


data = parse_input(raw_data)
N, M = len(data), len(data[0])


def check_low(i, j):
    val = data[i][j]
    cur = float("inf")
    for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if 0 <= ni < N and 0 <= nj < M:
            cur = min(cur, data[ni][nj])
            if cur <= val:
                return 0
    return val + 1


def part_one(data):
    res = 0
    for i in range(N):
        for j in range(M):
            res += check_low(i, j)
    return res


seen = set()


def flood_fill(i, j):
    res = 0
    q = deque([(i, j)])
    seen.add((i, j))
    while q:
        ci, cj = q.popleft()
        res += 1
        for ni, nj in ((ci + 1, cj), (ci - 1, cj), (ci, cj + 1), (ci, cj - 1)):
            if 0 <= ni < N and 0 <= nj < M and data[ni][nj] != 9 and (ni, nj) not in seen:
                q.append((ni, nj))
                seen.add((ni, nj))
    return res


def part_two(data):
    res = []
    for i in range(N):
        for j in range(M):
            if data[i][j] == 9 or (i, j) in seen:
                continue
            res.append(flood_fill(i, j))
    res.sort()
    return res[-1] * res[-2] * res[-3]


print(f"Part 1: {part_one(data)}")  # 591
print(f"Part 2: {part_two(data)}")  # 1113424
