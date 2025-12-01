import re


def parse_input():
    with open("01.txt", "r") as file:
        data = file.read()
    return [
        int(x.replace("L", "-").replace("R", "")) for x in re.findall(r"[RL]\d+", data)
    ]


def solve(pt2=False):
    rotations = parse_input()
    pos = 50
    res = 0
    for rot in rotations:
        cur, pos, prev = *divmod(pos + rot, 100), pos
        if not pt2 and pos == 0:
            res += 1
        if pt2:
            res += abs(cur)
            if rot < 0:
                res += (pos == 0) - (prev == 0)
    return res


print(f"Part 1: {solve()}")
print(f"Part 2: {solve(pt2=True)}")
