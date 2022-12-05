with open("19.txt", "r") as file:
    data = file.read()

MAZE = [list(line) for line in data.split("\n")]


def get_char(pos):
    return MAZE[int(pos.imag)][int(pos.real)]


def change_direction(pos, dir):
    cand = dir * 1j
    if get_char(pos + cand) != " ":
        return cand
    return dir * -1j


def solve():
    pos = MAZE[0].index("|") + 0j
    dir = 1j
    res = []
    steps = 0
    c = get_char(pos)
    while c != " ":
        steps += 1
        if c.isalpha():
            res.append(c)
        elif c == "+":
            dir = change_direction(pos, dir)
        pos += dir
        c = get_char(pos)
    return "".join(res), steps


part_one, part_two = solve()

print(f"Part 1: {part_one}")  # RUEDAHWKSM
print(f"Part 2: {part_two}")  # 17264
