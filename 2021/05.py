import re
from collections import Counter

with open('05.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    lines = re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', raw_data)
    return [list(map(int, line)) for line in lines]


data = parse_input(raw_data)


def straight_lines(data):
    points = Counter()
    for x1, y1, x2, y2 in data:
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for i in range(y1, y2+1):
                points[(x1, i)] += 1
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for i in range(x1, x2+1):
                points[(i, y1)] += 1
    return points


def diagonal_lines(data):
    points = Counter()
    for x1, y1, x2, y2 in data:
        if x1 != x2 and y1 != y2:
            while x1 != x2:
                points[(x1, y1)] += 1
                x1 += 1 if x1 < x2 else -1
                y1 += 1 if y1 < y2 else -1
            points[(x1, y1)] += 1
    return points


def part_one(data):
    points = straight_lines(data)
    return sum(v > 1 for v in points.values())


def part_two(data):
    points = straight_lines(data) + diagonal_lines(data)
    return sum(v > 1 for v in points.values())


print(f'Part 1: {part_one(data)}')  # 7438
print(f'Part 2: {part_two(data)}')  # 21406
