from collections import Counter

with open('06.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    return list(map(int, raw_data.split(',')))


data = parse_input(raw_data)


def step(cur):
    res = Counter()
    for i in range(6):
        res[i] = cur[i+1]
    res[6] = cur[0] + cur[7]
    res[7] = cur[8]
    res[8] = cur[0]
    return res


def part_one(data):
    fish = Counter(data)
    for _ in range(80):
        fish = step(fish)
    return sum(fish.values())


def part_two(data):
    fish = Counter(data)
    for _ in range(256):
        fish = step(fish)
    return sum(fish.values())


print(f'Part 1: {part_one(data)}')  # 391888
print(f'Part 2: {part_two(data)}')  # 1754597645339
