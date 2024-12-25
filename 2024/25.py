def parse_input():
    with open("25.txt", "r") as file:
        data = file.read()
    locks, keys = [], []
    for schematic in data.split("\n\n"):
        cur = {i for i, c in enumerate(schematic) if c == "#"}
        if schematic.startswith("#####"):
            locks.append(cur)
        else:
            keys.append(cur)
    return locks, keys


LOCKS, KEYS = parse_input()


def part_one():
    return sum(not lock & key for lock in LOCKS for key in KEYS)


print(f"Part 1: {part_one()}")
