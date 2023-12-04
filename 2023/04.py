import re
from collections import defaultdict

with open("04.txt", "r") as file:
    data = file.read().strip().split("\n")


def num_winners(game):
    a, b = game.split(":")[1].strip().split(" | ")
    a, b = re.findall(r"(\d+)", a), re.findall(r"(\d+)", b)
    return len(set(a) & set(b))


def part_one(data):
    return sum(1 << (x - 1) for game in data if (x := num_winners(game)))


def part_two(data):
    copies = defaultdict(lambda: 1)
    for i, game in enumerate(data):
        for di in range(1, num_winners(game) + 1):
            copies[i + di] += copies[i]
    return sum(copies.values())


print(f"Part 1: {part_one(data)}")  # 22897
print(f"Part 2: {part_two(data)}")  # 5095824
