with open("08.txt", "r") as file:
    raw_data = file.read().strip().split("\n")

DATA = raw_data


def part_one():
    return sum(map(lambda x: len(x) - len(eval(x)), DATA))


def part_two():
    return sum(map(lambda x: x.count(r'"') + x.count("\\") + 2, DATA))


print(f"Part 1: {part_one()}")  # 1342
print(f"Part 2: {part_two()}")  # 2074
