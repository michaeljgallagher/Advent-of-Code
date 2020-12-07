from collections import defaultdict, deque
import re

with open('07.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    bags = re.findall(r'([a-z]+ [a-z]+) bags contain (.+)', data)
    pattern = re.compile(r'(\d+) ([a-z]+ [a-z]+) bag')
    graph = {bag: {nested_bag: int(v) for v, nested_bag in pattern.findall(nested_bags)} for bag, nested_bags in bags}
    return graph


def create_reverse_graph(graph):
    rev = defaultdict(list)
    for k, v in graph.items():
        for new_key in v.keys():
            rev[new_key].append(k)
    return rev


def part_one(rev):
    seen = set()
    def dfs(bag):
        seen.add(bag)
        for nested_bag in rev[bag]:
            dfs(nested_bag)
    dfs('shiny gold')
    return len(seen) - 1  # remove one for 'shiny gold'


def part_two(graph):
    def dfs(bag):
        return 1 + sum((v * dfs(k)) for k, v in graph[bag].items())
    return dfs('shiny gold') - 1  # remove one for 'shiny gold'


graph = parse_input(data)
rev_graph = create_reverse_graph(graph)

print(f'Part 1: {part_one(rev_graph)}')  # 372
print(f'Part 2: {part_two(graph)}')  # 8015
