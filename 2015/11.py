from itertools import groupby

INPUT = "cqjxjnds"


def has_straight(s):
    nums = list(map(ord, s))
    for x, y, z in zip(nums, nums[1:], nums[2:]):
        if x == y - 1 == z - 2:
            return True
    return False


def no_invalids(s):
    return not any(c in "iol" for c in s)


def has_two_pairs(s):
    cur = None
    cnt = 0
    for c, grp in groupby(s):
        if c != cur and len(list(grp)) == 2:
            cur = c
            cnt += 1
    return cnt >= 2


def next_pw(s):
    p = list(s)
    while True:
        i = -1
        while p[i] == "z":
            p[i] = "a"
            i -= 1
        p[i] = chr(ord(p[i]) + 1)
        yield "".join(p)


def next_valid_pw(s):
    while True:
        s = next(next_pw(s))
        if has_straight(s) and no_invalids(s) and has_two_pairs(s):
            yield s


def part_one():
    return next(next_valid_pw(INPUT))


def part_two():
    res = next_valid_pw(INPUT)
    next(res)
    return next(res)


print(f"Part 1: {part_one()}")  # cqjxxyzz
print(f"Part 2: {part_two()}")  # cqkaabcc
