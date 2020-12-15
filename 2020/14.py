import re
from collections import defaultdict

with open('14.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    res = defaultdict(list)
    mask = None
    for line in data.split('\n'):
        if line[:4] == 'mask':
            mask = line[-36:]
        if line[:3] =='mem':
            match = re.match(r'mem\[(\d+)\] = (\d+)', line)
            res[mask].append((int(match.group(1)), int(match.group(2))))
    return res


def bitmask(mask, num):
    num = bin(num)[2:].zfill(36)
    res = [num[i] if v=='X' else v for i, v in enumerate(mask)]
    return int(''.join(res), 2)


def bitmask_two(mask, num):
    num = bin(num)[2:].zfill(36)
    res = []
    count = mask.count('X')
    new = ''.join('{}' if v=='X' else '1' if v=='1' else num[i] for i, v in enumerate(mask))
    for n in range(2**count):
        n = bin(n)[2:].zfill(count)
        res.append(new.format(*n))
    return [int(x, 2) for x in res]


def part_one(data):
    res = {}
    for mask, ints in data.items():
        for k, v in ints:
            res[k] = bitmask(mask, v)
    return sum(res.values())


def part_two(data):
    res = {}
    for mask, ints in data.items():
        for k, v in ints:
            for addr in bitmask_two(mask, k):
                res[addr] = v
    return sum(res.values())


data = parse_input(data)
print(f'Part 1: {part_one(data)}')  # 6513443633260
print(f'Part 2: {part_two(data)}')  # 3442819875191
