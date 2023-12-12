from functools import cache

with open("12.txt", "r") as file:
    data = file.read().strip()

RECORDS = [
    (x, tuple(map(int, y.split(","))))
    for row in data.split("\n")
    for x, y in [row.split(" ")]
]


@cache
def dp(seq, nums):
    if not seq:
        return nums == ()
    if not nums:
        return "#" not in seq
    res = 0
    if seq[0] in ".?":
        res += dp(seq[1:], nums)
    if seq[0] in "#?":
        n, r = len(seq), nums[0]
        if r <= n and "." not in seq[:r] and (r == n or seq[r] != "#"):
            res += dp(seq[r + 1 :], nums[1:])
    return res


def part_one():
    return sum(dp(seq, nums) for seq, nums in RECORDS)


def part_two():
    return sum(
        dp(seq, nums)
        for seq, nums in (
            ("?".join(seq for _ in range(5)), tuple(nums * 5)) for seq, nums in RECORDS
        )
    )


print(f"Part 1: {part_one()}")  # 7670
print(f"Part 2: {part_two()}")  # 157383940585037
