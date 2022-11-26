import hashlib
from collections import deque

PASSCODE = "ioramepc"


def md5(s):
    return hashlib.md5(s.encode()).hexdigest()[:4]


def solve(pt2=False):
    q = deque([(0, 0, "")])
    res = None
    while q:
        i, j, path = q.popleft()
        if i == j == 3:
            if not pt2:
                return path
            res = path
            continue
        u, d, l, r = md5(PASSCODE + path)
        if i > 0 and u in "bcdef":
            q.append((i - 1, j, path + "U"))
        if i < 3 and d in "bcdef":
            q.append((i + 1, j, path + "D"))
        if j > 0 and l in "bcdef":
            q.append((i, j - 1, path + "L"))
        if j < 3 and r in "bcdef":
            q.append((i, j + 1, path + "R"))
    return len(res)


print(f"Part 1: {solve()}")  # RDDRULDDRR
print(f"Part 2: {solve(True)}")  # 766
