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
    graph = {}
    data = [0] + data
    for i, x in enumerate(data):
        graph[x] = [y for y in data[i+1:i+4] if 0 < y-x <= 3]
    graph[max(data)] = [max(data)+3]
    return graph


def part_two(data):
    graph = make_graph(data)
    @lru_cache(None)
    def dfs(node):
        if node not in graph.keys():
            return 1
        return sum(dfs(nnode) for nnode in graph[node])
    return dfs(0)


data = parse_input(data)
print(f'Part 1: {part_one(data)}')  # 2376
print(f'Part 2: {part_two(data)}')  # 129586085429248
