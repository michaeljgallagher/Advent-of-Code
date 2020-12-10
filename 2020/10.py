from functools import lru_cache

with open('10.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    jolts = sorted(list(map(int, data.split('\n'))))
    return [0] + jolts + [jolts[-1] + 3]


def part_one(data):
    diff = [data[i+1] - data[i] for i in range(len(data)-1)]
    a = diff.count(1)
    b = diff.count(3)
    return a * b


def make_graph(data):
    graph = {}
    for i, x in enumerate(data):
        graph[x] = [y for y in data[i+1:i+4] if 0 < y-x <= 3]
    return graph


def part_two(data):
    graph = make_graph(data)
    @lru_cache(None)
    def dfs(node):
        if not graph[node]:
            return 1
        return sum(dfs(nnode) for nnode in graph[node])
    return dfs(0)


def part_two_alt(data):
    dp = {0: 1}
    for x in data[1:]:
        dp[x] = dp.get(x-1, 0) + dp.get(x-2, 0) + dp.get(x-3, 0)
    return dp[data[-1]]


data = parse_input(data)
print(f'Part 1: {part_one(data)}')  # 2376
print(f'Part 2: {part_two(data)}')  # 129586085429248
print(f'Part 2 alt: {part_two_alt(data)}')  # 0.000048 seconds, improved from 0.000497 seconds
