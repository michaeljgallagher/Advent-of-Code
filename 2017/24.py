def parse_input():
    with open("24.txt", "r") as file:
        data = file.read()
    return sorted(sorted(map(int, line.split("/"))) for line in data.splitlines())


PORTS = parse_input()


def bt(cur, seen, pt2=False):
    res = 0
    max_len = 0
    for i, (u, v) in enumerate(PORTS):
        if i in seen:
            continue
        if v == cur:
            u, v = v, u
        if u != cur:
            continue
        strength, length = bt(v, seen | {i}, pt2)
        strength += u + v
        length += 1
        if pt2:
            if length == max_len:
                res = max(res, strength)
            if length > max_len:
                max_len = length
                res = strength
        else:
            res = max(res, strength)
    return res, max_len


def part_one():
    return bt(0, set())[0]


def part_two():
    return bt(0, set(), True)[0]


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
