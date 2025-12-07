from collections import defaultdict


def parse_input():
    with open("07.txt", "r") as f:
        data = f.read()
    return data.splitlines()


def solve(pt2=False):
    grid = parse_input()
    start = (0, grid[0].index("S"))
    n = len(grid)
    dp = defaultdict(int)
    dp[start] += 1
    res = int(pt2)  # pt2 starts with 1 path
    for _ in range(n - 1):
        ndp = defaultdict(int)
        for (i, j), cur in dp.items():
            if i == n - 1:
                continue
            inc = cur if pt2 else 1
            if grid[i + 1][j] == "^":
                res += inc
                ndp[(i + 1, j - 1)] += inc
                ndp[(i + 1, j + 1)] += inc
            else:
                ndp[(i + 1, j)] += inc
        dp = ndp
    return res


print(f"Part 1: {solve()}")
print(f"Part 2: {solve(pt2=True)}")
