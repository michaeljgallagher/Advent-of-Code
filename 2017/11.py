with open("11.txt", "r") as file:
    data = file.read().strip()

DIRS = {
    "nw": -1,
    "ne": 1 - 1j,
    "sw": -1 + 1j,
    "se": 1,
    "n": -1j,
    "s": 1j,
}


def calc_distance(pos):
    q, r = int(pos.real), int(pos.imag)
    return (abs(q) + abs(r) + abs(q + r)) // 2


def take_steps(data):
    pos = 0j
    res = 0
    for step in data.split(","):
        pos += DIRS[step]
        res = max(res, calc_distance(pos))
    return calc_distance(pos), res


part_one, part_two = take_steps(data)

print(f"Part 1: {part_one}")  # 685
print(f"Part 2: {part_two}")  # 1457
