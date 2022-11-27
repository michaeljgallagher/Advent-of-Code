with open("05.txt", "r") as file:
    data = file.read().strip()


def calc_jumps(instructions, part_two=False):
    i = res = 0
    while 0 <= i < len(instructions):
        ni = i + instructions[i]
        instructions[i] += 1 - 2 * (part_two and instructions[i] >= 3)
        i = ni
        res += 1
    return res


def part_one():
    return calc_jumps(list(map(int, data.split("\n"))))


def part_two():
    return calc_jumps(list(map(int, data.split("\n"))), part_two=True)


print(f"Part 1: {part_one()}")  # 315613
print(f"Part 2: {part_two()}")  # 22570529
