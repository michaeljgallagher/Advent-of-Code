from functools import cache


def parse_input():
    with open("21.txt", "r") as file:
        data = file.read()
    return {
        tuple(x.split("/")): tuple(y.split("/"))
        for line in data.splitlines()
        for x, y in [line.split(" => ")]
    }


RULES = parse_input()


def rotate(pattern):
    return tuple("".join(row) for row in zip(*pattern[::-1]))


@cache
def get_rule(pattern):
    for _ in range(4):
        if pattern in RULES:
            return RULES[pattern]
        pattern = rotate(pattern)
    pattern = tuple(reversed(pattern))
    for _ in range(4):
        if pattern in RULES:
            return RULES[pattern]
        pattern = rotate(pattern)


def step(pattern):
    n = len(pattern)
    k = 2 + (n & 1)
    row_sz = n // k
    squares = []
    for i in range(row_sz):
        cur = []
        for j in range(row_sz):
            square = tuple(
                "".join(pattern[i * k + di][j * k + dj] for dj in range(k))
                for di in range(k)
            )
            cur.append(get_rule(square))
        squares.append(cur)
    return tuple("".join(line) for square in squares for line in zip(*square))


def part_one():
    pattern = (".#.", "..#", "###")
    for _ in range(5):
        pattern = step(pattern)
    return sum(row.count("#") for row in pattern)


def part_two():
    pattern = (".#.", "..#", "###")
    for _ in range(18):
        pattern = step(pattern)
    return sum(row.count("#") for row in pattern)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
