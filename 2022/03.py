with open("03.txt", "r") as file:
    data = file.read().strip()

RUCKSACKS = data.split("\n")


def calc_priority(group):
    return sum(
        ord(c) - ord("a") + 1
        if c.islower()
        else ord(c) - ord("A") + 27
        for c in group
    )


def part_one():
    res = 0
    for rucksack in RUCKSACKS:
        m = len(rucksack) >> 1
        a, b = rucksack[:m], rucksack[m:]
        res += calc_priority(set(a) & set(b))
    return res


def part_two():
    res = 0
    for i in range(0, len(RUCKSACKS), 3):
        a, b, c = RUCKSACKS[i : i + 3]
        res += calc_priority(set(a) & set(b) & set(c))
    return res


print(f"Part 1: {part_one()}")  # 7826
print(f"Part 2: {part_two()}")  # 2577
