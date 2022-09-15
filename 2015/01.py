with open("01.txt", "r") as file:
    raw_data = file.read().strip()


def part_one(data):
    return sum(1 - 2 * (c != "(") for c in data)


def part_two(data):
    res = 0
    for i, c in enumerate(data):
        res += 1 - 2 * (c != "(")
        if res == -1:
            return i + 1


print(f"Part 1: {part_one(raw_data)}")  # 74
print(f"Part 2: {part_two(raw_data)}")  # 1795
