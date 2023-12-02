import re
from collections import Counter, defaultdict
from math import prod

with open("02.txt", "r") as file:
    data = file.read().strip().split("\n")


def parse_game(game):
    cubes = defaultdict(int)
    for n, color in re.findall(r"(\d+) (\w+)", game):
        cubes[color] = max(cubes[color], int(n))
    return cubes


def is_possible(game):
    bag = Counter({"red": 12, "green": 13, "blue": 14})
    cubes = Counter(parse_game(game))
    return not any(v > 0 for v in (cubes - bag).values())


def find_power(game):
    return prod(parse_game(game).values())


def part_one(data):
    return sum(i for i, game in enumerate(data, start=1) if is_possible(game))


def part_two(data):
    return sum(find_power(game) for game in data)


print(f"Part 1: {part_one(data)}")  # 2085
print(f"Part 2: {part_two(data)}")  # 79315
