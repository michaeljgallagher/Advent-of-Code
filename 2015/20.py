from itertools import count

INPUT = 36000000


def solve(target, upper):
    dp = [1] * target
    for i in count(2):
        for j in range(min(target // i, upper)):
            dp[i * j] += i
        if dp[i] >= target:
            return i


print(f"Part 1: {solve(INPUT//10, INPUT//10)}")  # 831600
print(f"Part 2: {solve(INPUT//11, 50)}")  # 884520
