import re
from collections import Counter

with open('14.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    template = raw_data.split('\n')[0]
    pairs = re.findall(r'(.+) -> (.+)', raw_data)
    return template, dict(pairs)


TEMPLATE, RULES = parse_input(raw_data)


def step(count):
    res = Counter()
    for k in count:
        res[k[0] + RULES[k]] += count[k]
        res[RULES[k] + k[1]] += count[k]
    return res


def run_n_steps(n):
    cur = Counter()
    for i in range(len(TEMPLATE) - 1):
        cur[TEMPLATE[i:i+2]] += 1

    for _ in range(n):
        nxt = step(cur)
        cur = nxt

    res = Counter()
    for k in cur:
        res[k[0]] += cur[k]
    res[TEMPLATE[-1]] += 1

    return max(res.values()) - min(res.values())


def part_one():
    return run_n_steps(10)


def part_two():
    return run_n_steps(40)


print(f'Part 1: {part_one()}')  # 2745
print(f'Part 2: {part_two()}')  # 3420801168962
