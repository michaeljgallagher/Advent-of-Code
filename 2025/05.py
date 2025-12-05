def parse_input():
    with open("05.txt", "r") as f:
        data = f.read()
    a, b = data.split("\n\n")
    a = sorted(tuple(map(int, line.split("-"))) for line in a.splitlines())
    ranges = [a[0]]
    for l, r in a[1:]:
        pl, pr = ranges[-1]
        if l <= pr:
            ranges[-1] = (pl, max(pr, r))
        else:
            ranges.append((l, r))
    ingredients = list(map(int, b.splitlines()))
    return ranges, ingredients


RANGES, INGREDIENTS = parse_input()


def part_one():
    return sum(any(l <= i <= r for l, r in RANGES) for i in INGREDIENTS)


def part_two():
    return sum(r - l + 1 for l, r in RANGES)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
