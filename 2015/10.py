from itertools import groupby

INPUT = "1321131112"


def look_and_say(s, reps):
    for _ in range(reps):
        cur = []
        for c, grp in groupby(s):
            cur.append(str(len(list(grp))) + c)
        s = "".join(cur)
    return len(s)


def part_one():
    return look_and_say(INPUT, 40)


def part_two():
    return look_and_say(INPUT, 50)


print(f"Part 1: {part_one()}")  # 492982
print(f"Part 2: {part_two()}")  # 6989950
