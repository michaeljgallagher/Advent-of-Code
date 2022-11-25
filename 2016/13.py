from collections import deque

INPUT = 1362


def is_open(x, y):
    n = x * x + 3 * x + 2 * x * y + y + y * y + INPUT
    return not n.bit_count() & 1


def part_one():
    q = deque([(1, 1)])
    seen = set(((1, 1)))
    res = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if (i, j) == (31, 39):
                return res
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if (
                    ni >= 0
                    and nj >= 0
                    and is_open(ni, nj)
                    and (ni, nj) not in seen
                ):
                    q.append((ni, nj))
                    seen.add((ni, nj))
        res += 1


def part_two():
    q = deque([(1, 1)])
    seen = set()
    for _ in range(51):
        for _ in range(len(q)):
            i, j = q.popleft()
            seen.add((i, j))
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if (
                    ni >= 0
                    and nj >= 0
                    and is_open(ni, nj)
                    and (ni, nj) not in seen
                ):
                    q.append((ni, nj))
    return len(seen)


print(f"Part 1: {part_one()}")  # 82
print(f"Part 2: {part_two()}")  # 138
