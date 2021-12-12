from collections import defaultdict

with open("12.txt", "r") as file:
    raw_data = file.read()


def parse_input(raw_data):
    res = defaultdict(list)
    for row in raw_data.split("\n"):
        u, v = row.split('-')
        res[u].append(v)
        res[v].append(u)
    return res


GRAPH = parse_input(raw_data)


def dfs(node, seen, two=False):
    if node == 'end':
        return 1
    if node == 'start' and seen:
        return 0
    if node.islower() and node in seen:
        if two:
            two = False
        else:
            return 0
    seen = seen | {node}
    res = 0
    for nei in GRAPH[node]:
        res += dfs(nei, seen, two)
    return res


def part_one():
    return dfs('start', set())


def part_two():
    return dfs('start', set(), True)


print(f"Part 1: {part_one()}")  # 3369
print(f"Part 2: {part_two()}")  # 85883
