with open("03.txt", "r") as file:
    data = file.read().strip()

TRIANGLES = [tuple(map(int, line.split())) for line in data.split("\n")]


def possible(*args):
    return sum(args) > 2 * max(args)


def part_one():
    return sum(possible(*triangle) for triangle in TRIANGLES)


def part_two():
    flatten = [x[i] for i in range(3) for x in TRIANGLES]
    return sum(possible(*flatten[i : i + 3]) for i in range(0, len(flatten), 3))


print(f"Part 1: {part_one()}")  # 1032
print(f"Part 2: {part_two()}")  # 1838
