from collections import defaultdict

with open('24.txt', 'r') as file:
    data = file.read().split('\n')

DIRS = {
    'nw': 0 - 1j,
    'ne': 1 - 1j,
    'sw': -1 + 1j,
    'se': 0 + 1j,
    'e': 1 + 0j,
    'w': -1 + 0j,
}


def calc_tile(line):
    res = 0 + 0j
    i = 0
    while i < len(line):
        if line[i] in {'n', 's'}:
            cur = line[i:i+2]
            i += 2
        else:
            cur = line[i]
            i += 1
        res += DIRS[cur]
    return res


def find_black(data):
    res = defaultdict(int)
    for line in data:
        pos = calc_tile(line)
        res[pos] ^= 1
    return {k for k, v in res.items() if v == 1}


def find_neighbors(tiles):
    neighbors = defaultdict(int)
    for tile in tiles:
        for delta in DIRS.values():
            cur = tile + delta
            neighbors[cur] += 1
    return neighbors


def step(tiles):
    new_black = set()
    neighbors = find_neighbors(tiles)
    for k, v in neighbors.items():
        if (v == 2 and k not in tiles) or (k in tiles and 1 <= v <= 2):
            new_black.add(k)
    return new_black


def part_one(data):
    return len(find_black(data))


def part_two(data):
    tiles = find_black(data)
    for _ in range(100):
        tiles = step(tiles)
    return len(tiles)


print(f'Part 1: {part_one(data)}')  # 388
print(f'Part 2: {part_two(data)}')  # 4002
