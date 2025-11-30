from collections import deque
from math import lcm


def parse_input():
    with open("24.txt", "r") as file:
        data = file.read()
    lines = data.splitlines()
    blizzards = []
    for i, row in enumerate(lines):
        for j, c in enumerate(row):
            if c in "^v<>":
                blizzards.append((i, j, c))
    h, w = len(lines), len(lines[0])
    start = (0, lines[0].index("."))
    goal = (h - 1, lines[-1].index("."))
    return blizzards, h, w, start, goal


def precompute_blizzards(blizzards, h, w):
    inner_h = h - 2
    inner_w = w - 2
    cycle = lcm(inner_h, inner_w)
    cache = {}
    for t in range(cycle):
        pos = set()
        for i, j, d in blizzards:
            if d == "^":
                ni = ((i - 1 - t) % inner_h) + 1
                nj = j
            elif d == "v":
                ni = ((i - 1 + t) % inner_h) + 1
                nj = j
            elif d == "<":
                ni = i
                nj = ((j - 1 - t) % inner_w) + 1
            elif d == ">":
                ni = i
                nj = ((j - 1 + t) % inner_w) + 1
            pos.add((ni, nj))
        cache[t] = pos
    return cache, cycle


def is_valid(i, j, h, w, start, goal):
    if (i, j) == start or (i, j) == goal:
        return True
    if i <= 0 or i >= h - 1 or j <= 0 or j >= w - 1:
        return False
    return True


def find_path(cache, cycle, h, w, start, goal, start_t=0):
    q = deque([(start[0], start[1], start_t)])
    seen = {(start[0], start[1], start_t % cycle)}
    while q:
        i, j, t = q.popleft()
        if (i, j) == goal:
            return t
        next_t = t + 1
        blizzard_pos = cache[next_t % cycle]
        for ni, nj in (i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
            if is_valid(ni, nj, h, w, start, goal):
                if (ni, nj) not in blizzard_pos:
                    state = (ni, nj, next_t % cycle)
                    if state not in seen:
                        seen.add(state)
                        q.append((ni, nj, next_t))
    return -1


def part_one():
    blizzards, h, w, start, goal = parse_input()
    cache, cycle = precompute_blizzards(blizzards, h, w)
    return find_path(cache, cycle, h, w, start, goal)


def part_two():
    blizzards, h, w, start, goal = parse_input()
    cache, cycle = precompute_blizzards(blizzards, h, w)
    t1 = find_path(cache, cycle, h, w, start, goal, 0)
    t2 = find_path(cache, cycle, h, w, goal, start, t1)
    t3 = find_path(cache, cycle, h, w, start, goal, t2)
    return t3


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
