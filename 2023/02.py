from collections import Counter, defaultdict
from math import prod

with open("02.txt", "r") as file:
    data = file.read().strip().split("\n")


def parse_game(game):
    res = []
    sets = game.split(":")[1].strip()
    for set in sets.split(";"):
        c = Counter()
        for cubes in set.split(", "):
            n, cur = cubes.strip().split(" ")
            c[cur] = int(n)
        res.append(c)
    return res


def is_possible(game, bag):
    sets = parse_game(game)
    for set in sets:
        if any(v > 0 for v in (set - bag).values()):
            return False
    return True


def find_power(game):
    cubes = defaultdict(int)
    sets = parse_game(game)
    for set in sets:
        for color in ("red", "green", "blue"):
            cubes[color] = max(cubes[color], set[color])
    return prod(cubes.values())


def part_one(data):
    return sum(
        i
        for i, game in enumerate(data, start=1)
        if is_possible(game, Counter({"red": 12, "green": 13, "blue": 14}))
    )


def part_two(data):
    return sum(find_power(game) for game in data)


print(f"Part 1: {part_one(data)}")  # 2085
print(f"Part 2: {part_two(data)}")  # 79315
