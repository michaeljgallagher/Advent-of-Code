from collections import deque


def parse_input():
    with open("18.txt", "r") as file:
        data = file.read()
    return {tuple(map(int, row.split(","))) for row in data.splitlines()}


def solve(pt2=False):
    tiles = parse_input()
    top = min(i for i, _, _ in tiles)
    bottom = max(i for i, _, _ in tiles)
    left = min(j for _, j, _ in tiles)
    right = max(j for _, j, _ in tiles)
    front = min(k for _, _, k in tiles)
    back = max(k for _, _, k in tiles)

    def is_exterior(i, j, k):
        q = deque([(i, j, k)])
        seen = {(i, j, k)}
        while q:
            i, j, k = q.popleft()
            if i < top or i > bottom or j < left or j > right or k < front or k > back:
                return True
            for ni, nj, nk in (
                (i - 1, j, k),
                (i + 1, j, k),
                (i, j - 1, k),
                (i, j + 1, k),
                (i, j, k - 1),
                (i, j, k + 1),
            ):
                if (ni, nj, nk) not in seen and (ni, nj, nk) not in tiles:
                    seen.add((ni, nj, nk))
                    q.append((ni, nj, nk))
        return False

    res = 0
    for i, j, k in tiles:
        for ni, nj, nk in (
            (i - 1, j, k),
            (i + 1, j, k),
            (i, j - 1, k),
            (i, j + 1, k),
            (i, j, k - 1),
            (i, j, k + 1),
        ):
            if pt2:
                res += int((ni, nj, nk) not in tiles and is_exterior(ni, nj, nk))
            else:
                res += int((ni, nj, nk) not in tiles)
    return res


print(f"Part 1: {solve()}")
print(f"Part 2: {solve(pt2=True)}")
