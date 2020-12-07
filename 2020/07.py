from collections import defaultdict, deque

with open('07.txt', 'r') as file:
    data = file.read().split('\n')


def parse_input(data):
    '''
    construct a graph
    {bag_color: {bag_color, amount}}
    '''
    rules = [[y.strip() for y in x.split('contain')] for x in data]
    graph = {' '.join(x[0].split()[:-1]): x[1:] for x in rules}
    for k, v in graph.items():
        new = {}
        cur = v[0].split(', ')
        for s in cur:
            if s == 'no other bags.': continue
            key = (' '.join(s[2:].split()[:-1]))
            val = int(s[0])
            new[key] = val
        graph[k] = new
    return graph


def create_reverse_graph(graph):
    rev = defaultdict(list)
    for k, v in graph.items():
        for new_key in v.keys():
            rev[new_key].append(k)
    return rev


def part_one(rev):
    q = deque(rev['shiny gold'])
    seen = set(['shiny gold'])
    while q:
        cur = q.popleft()
        if cur not in seen:
            q += deque(rev[cur])
            seen.add(cur)
    return len(seen) - 1  # remove one for 'shiny gold'


def part_two(graph):
    def dfs(graph, bag):
        if not graph[bag]:
            return 1
        return 1 + sum((v * dfs(graph, k)) for k, v in graph[bag].items())
    return dfs(graph, 'shiny gold') - 1  #remove one for 'shiny gold'


graph = parse_input(data)
rev_graph = create_reverse_graph(graph)

print(f'Part 1: {part_one(rev_graph)}')  # 372
print(f'Part 2: {part_two(graph)}')  # 8015