with open("02.txt", "r") as file:
    raw_data = file.read().strip()


def parse_input(raw_data):
    return [tuple(map(int, line.split("x"))) for line in raw_data.split("\n")]


data = parse_input(raw_data)


def get_wrapping_area(dims):
    l, w, h = dims
    a, b, c = l * w, l * h, w * h
    return 2 * (a + b + c) + min(a, b, c)


def get_ribbon_len(dims):
    a, b, c = sorted(dims)
    return 2 * (a + b) + (a * b * c)


def part_one(data):
    return sum(get_wrapping_area(dims) for dims in data)


def part_two(data):
    return sum(get_ribbon_len(dims) for dims in data)


print(f"Part 1: {part_one(data)}")  # 1588178
print(f"Part 2: {part_two(data)}")  # 3783758
