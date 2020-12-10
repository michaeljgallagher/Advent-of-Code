from functools import lru_cache

with open('10.txt', 'r') as file:
    data = file.read()

def parse_input(data):
    return sorted(list(map(int, data.split('\n'))))


def part_one(data):
    data = [0] + data
    diff = [data[i+1] - data[i] for i in range(len(data)-1)]
    a = diff.count(1)
    b = diff.count(3) + 1  # add 3 for the wall outlet
    return a * b


def make_graph(data):
    res = {}
    data = [0] + data
    for x in data:
        res[x] = [i for i in data if 0 < i-x <= 3]
    res[max(data)] = [max(data)+3]
    return res


def part_two(data):
    graph = make_graph(data)
    @lru_cache(None)
    def dfs(node):
        if node not in graph.keys():
            return 1
        options = graph[node]
        cur = 0
        for new_node in options:
            cur += dfs(new_node)
        return cur
    return dfs(0)


data = parse_input(data)
print(f'Part 1: {part_one(data)}')  # 2376
print(f'Part 2: {part_two(data)}')  # 129586085429248
