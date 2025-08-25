from collections import deque
from itertools import count


def adj(i, j):
    return [(i, j - 1), (i - 1, j), (i + 1, j), (i, j + 1)]


def parse_input():
    with open("15.txt", "r") as file:
        lines = file.read().splitlines()
    entities = {}
    walls = set()
    idx = 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                walls.add((j, i))
            elif c != ".":
                entities[(j, i)] = (idx, c == "E", 200)
                idx += 1
    return entities, walls


def bfs(start, entities, walls, elf, condition_func):
    i, j = start
    q = deque([(0, i, j)])
    visited = set()
    dist = None
    nearest = []
    while q:
        d, u, v = q.popleft()
        if (u, v) in visited:
            continue
        visited.add((u, v))
        if condition_func(u, v, elf, entities):
            if dist is None:
                dist = d
            elif d > dist:
                break
            nearest.append((u, v))
        for r in adj(u, v):
            if r in walls or (e := entities.get(r)) and e[1] == elf:
                continue
            q.append((d + 1, *r))
    return nearest


def find_enemies_in_range(u, v, elf, entities):
    return any(e[1] != elf for r in adj(u, v) if (e := entities.get(r)))


def is_adjacent_to_target(target):
    def check(u, v, elf, entities):
        return target in adj(u, v)

    return check


def get_enemies_in_range(pos, entities, elf):
    i, j = pos
    return [(u, v) for u in adj(i, j) if (v := entities.get(u)) and v[1] != elf]


def step(pos, entities, walls, elf):
    i, j = pos
    nearest_enemies = bfs((i, j), entities, walls, elf, find_enemies_in_range)
    if not nearest_enemies:
        return pos
    target = min(nearest_enemies, key=lambda a: a[::-1])
    nearest_moves = bfs(target, entities, walls, elf, is_adjacent_to_target((i, j)))
    if not nearest_moves:
        return pos
    npos = min(nearest_moves, key=lambda a: a[::-1])
    entities[npos] = entities.pop((i, j))
    return npos


def attack(pos, entities, elf, elf_attack_power):
    in_range = get_enemies_in_range(pos, entities, elf)
    if not in_range:
        return False
    in_range.sort(key=lambda a: (a[1][2], a[0][::-1]))
    u, (idx2, elf2, hp2) = in_range[0]
    attack_power = elf_attack_power if elf else 3
    hp2 -= attack_power
    if hp2 <= 0:
        if elf2 and elf_attack_power > 3:
            return -1
        entities.pop(u)
    else:
        entities[u] = idx2, elf2, hp2
    return True


def process_turn(pos, entities, walls, orig, elf_attack_power):
    i, j = pos
    if (i, j) not in entities:
        return None
    idx, elf, hp = entities[(i, j)]
    if idx != orig[(i, j)][0]:
        return None
    if not any(q[1] != elf for q in entities.values()):
        return "finish"
    in_range = get_enemies_in_range((i, j), entities, elf)
    if not in_range:
        new_pos = step((i, j), entities, walls, elf)
        i, j = new_pos
    return attack((i, j), entities, elf, elf_attack_power)


def simulate(elf_attack_power=3):
    entities, walls = parse_input()
    for rnd in count():
        orig = entities.copy()
        for i, j in sorted(entities, key=lambda a: a[::-1]):
            res = process_turn((i, j), entities, walls, orig, elf_attack_power)
            if res == "finish":
                return rnd * sum(e[2] for e in entities.values())
            elif res == -1:
                return -1


def part_one():
    return simulate()


def part_two():
    for i in count(4):
        if (res := simulate(i)) > 0:
            return res


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
