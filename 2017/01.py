with open("01.txt", "r") as file:
    data = file.read().strip()


def part_one():
    return sum(
        int(x)
        for x, y in zip(data, data[1:] + data[:1])
        if x == y
    )


def part_two():
    return sum(
        int(x)
        for x, y in zip(data, data[len(data) >> 1 :] + data[: len(data) >> 1])
        if x == y
    )


print(f"Part 1: {part_one()}")  # 1393
print(f"Part 2: {part_two()}")  # 1292
