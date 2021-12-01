from itertools import accumulate

with open('01.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    return list(map(int, raw_data.split("\n")))


data = parse_input(raw_data)


def part_one(data):
    return sum(data[i] > data[i - 1] for i in range(1, len(data)))


def part_two(data):
    cur = prev = sum(data[:3])
    res = 0
    for i in range(3, len(data)):
        cur += data[i] - data[i - 3]
        res += cur > prev
        prev = cur
    return res


print(f'Part 1: {part_one(data)}')  # 1446
print(f'Part 2: {part_two(data)}')  # 1486
