with open("10.txt", "r") as file:
    data = file.read().strip()


def parse_data(data):
    reg = [1]
    for line in data.split("\n"):
        reg.append(reg[-1])
        if x := line[5:]:
            reg.append(reg[-1] + int(x))
    return reg


REG = parse_data(data)


def part_one():
    return sum(
        cycle * x
        for cycle, x in enumerate(REG, 1)
        if cycle % 40 == 20
    )


def part_two():
    for cycle, x in enumerate(REG):
        print(
            "#" if abs(cycle % 40 - x) <= 1 else " ",
            end="" if (cycle + 1) % 40 else "\n",
        )


print(f"Part 1: {part_one()}")  # 11720
print(f"Part 2: {part_two()}")  # ERCREPCJ
