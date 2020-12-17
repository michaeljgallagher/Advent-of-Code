from collections import defaultdict

with open('17.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    return [list(line) for line in data.split('\n')]


data = parse_input(data)


def find_active(data):
    active = set()
    N, M = len(data), len(data[0])
    for i in range(N):
        for j in range(M):
            if data[i][j] == '#':
                active.add((i, j, 0))
    return active


def find_all_neighbors(active):
    neighbors = defaultdict(int)
    for cube in active:
        x, y, z = cube
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    if dx == dy == dz == 0:
                        continue
                    cur = (x+dx, y+dy, z+dz)
                    neighbors[cur] += 1
    return neighbors


def find_active_two(data):
    active = set()
    N, M = len(data), len(data[0])
    for i in range(N):
        for j in range(M):
            if data[i][j] == '#':
                active.add((i, j, 0, 0))
    return active


def find_all_neighbors_two(active):
    neighbors = defaultdict(int)
    for cube in active:
        x, y, z, w = cube
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    for dw in [-1, 0, 1]:
                        if dx == dy == dz == dw == 0:
                            continue
                        cur = (x+dx, y+dy, z+dz, w+dw)
                        neighbors[cur] += 1
    return neighbors


def run_cycle(active):
    new_active = set()
    neighbors = find_all_neighbors(active)
    for k, v in neighbors.items():
        if v == 3:
            new_active.add(k)
        elif v == 2 and k in active:
            new_active.add(k)
    return new_active


def run_cycle_two(active):
    new_active = set()
    neighbors = find_all_neighbors_two(active)
    for k, v in neighbors.items():
        if v == 3:
            new_active.add(k)
        elif v == 2 and k in active:
            new_active.add(k)
    return new_active


def part_one(data):
    active = find_active(data)
    for _ in range(6):
        active = run_cycle(active)
    return len(active)


def part_two(data):
    active = find_active_two(data)
    for _ in range(6):
        active = run_cycle_two(active)
    return len(active)


print(f'Part 1: {part_one(data)}')  # 252
print(f'Part 2: {part_two(data)}')  # 2160
