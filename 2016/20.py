with open("20.txt", "r") as file:
    data = file.read().strip()

IP_RANGES = sorted(
    tuple(map(int, line.split("-")))
    for line in data.split("\n")
)


def part_one(ips):
    res = 0
    for lo, hi in ips:
        if lo > res:
            return res
        res = max(res, hi + 1)
    return -1


def part_two(ips):
    res = cur = 0
    for lo, hi in ips:
        if lo > cur:
            res += lo - cur
        cur = max(cur, hi + 1)
    return res + (1 << 32) - cur


print(f"Part 1: {part_one(IP_RANGES)}")  # 32259706
print(f"Part 2: {part_two(IP_RANGES)}")  # 113
