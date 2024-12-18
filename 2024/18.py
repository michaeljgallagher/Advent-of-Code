import re
from collections import deque
from itertools import batched


def parse_input():
    with open("18.txt", "r") as file:
        data = file.read()
    return list(batched(map(int, re.findall(r"(\d+)", data)), 2))


BYTES = parse_input()
N = M = 71


def bfs(idx):
    q = deque([(0, 0)])
    seen = {(0, 0)} | set(BYTES[:idx])
    res = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if (i, j) == (N - 1, M - 1):
                return res
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    q.append((ni, nj))
        res += 1
    return -1


def part_one():
    return bfs(1024)


def part_two():
    l, r = 1025, len(BYTES) - 1
    while l < r:
        m = l + (r - l >> 1)
        if bfs(m) == -1:
            r = m
        else:
            l = m + 1
    return ",".join(map(str, BYTES[l - 1]))


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
