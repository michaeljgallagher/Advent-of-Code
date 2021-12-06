from collections import Counter

with open('06.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    return list(map(int, raw_data.split(',')))


data = parse_input(raw_data)


def step(cur):
    res = Counter()
    for k, v in cur.items():
        if k == 0:
            res[6] += v
            res[8] += v
        else:
            res[k-1] += v
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
