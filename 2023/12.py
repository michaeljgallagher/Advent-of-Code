from functools import cache

with open("12.txt", "r") as file:
    data = file.read().strip()

RECORDS = [
    (x, tuple(map(int, y.split(","))))
    for row in data.split("\n")
    for x, y in [row.split(" ")]
]


@cache
def dp(i, j, cur, seq, nums):
    if i == len(seq):
        return (j == len(nums) - 1 and nums[j] == cur) or (j == len(nums) and cur == 0)
    res = 0
    if seq[i] in "#?":
        res += dp(i + 1, j, cur + 1, seq, nums)
    if seq[i] in ".?":
        if cur == 0:
            res += dp(i + 1, j, 0, seq, nums)
        elif cur > 0 and j < len(nums) and nums[j] == cur:
            res += dp(i + 1, j + 1, 0, seq, nums)
    return res


def part_one():
    return sum(dp(0, 0, 0, seq, nums) for seq, nums in RECORDS)


def part_two():
    return sum(
        dp(0, 0, 0, seq, nums)
        for seq, nums in (
            ("?".join(seq for _ in range(5)), tuple(nums * 5)) for seq, nums in RECORDS
        )
    )


print(f"Part 1: {part_one()}")  # 7670
print(f"Part 2: {part_two()}")  # 157383940585037
