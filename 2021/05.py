import re
from collections import Counter

with open('05.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    lines = re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', raw_data)
    return [list(map(int, line)) for line in lines]


data = parse_input(raw_data)


def part_one(data):
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


def part_two(data):
    points = part_one(data)
    for x1, y1, x2, y2 in data:
        if x1 != x2 and y1 != y2:
            while x1 != x2:
                points[(x1, y1)] += 1
                x1 += 1 if x1 < x2 else -1
                y1 += 1 if y1 < y2 else -1
            points[(x1, y1)] += 1
    return points


print(f'Part 1: {sum(v > 1 for v in part_one(data).values())}')  # 7438
print(f'Part 2: {sum(v > 1 for v in part_two(data).values())}')  # 21406
