from collections import Counter

with open("01.txt", "r") as file:
    data = file.read().strip().splitlines()


def parse_input(data):
    left, right = [], []
    for row in data:
        l, r = row.split()
        left.append(int(l))
        right.append(int(r))
    return left, right


def part_one(left, right):
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def part_two(left, right):
    freq = Counter(right)
    return sum(x * freq[x] for x in left)


print(f"Part 1: {part_one(*parse_input(data))}")
print(f"Part 2: {part_two(*parse_input(data))}")
