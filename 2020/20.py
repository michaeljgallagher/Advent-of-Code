from collections import defaultdict

with open('20.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    tiles = {}
    for tile in data.split('\n\n'):
        cur = tile.split('\n')
        n = int(cur[0][-5:-1])
        tiles[n] = cur[1:]
    return tiles


tiles = parse_input(data)


def make_edge_dict(tiles):
    edge_dict = {}
    for k, v in tiles.items():
        edges = []
        edges += [v[0], v[0][::-1], v[-1], v[-1][::-1]]
        t = list(map(list, zip(*v)))
        for i, v in enumerate(t):
	        t[i] = ''.join(v)
        edges += [t[0], t[0][::-1], t[-1], t[-1][::-1]]
        edge_dict[k] = set(edges)
    return edge_dict


edge_dict = make_edge_dict(tiles)


def part_one(edge_dict):
    neighbors = defaultdict(set)
    for k, v in edge_dict.items():
        for n, x in edge_dict.items():
            if k == n:
                continue
            if v&x:
                neighbors[k].add(n)
                neighbors[n].add(k)
    res = 1
    for k, v in neighbors.items():
        if len(v) == 2:
            res *= k
    return res


def part_two(data):
    return


print(f'Part 1: {part_one(edge_dict)}')  # 23386616781851
print(f'Part 2: {part_two(data)}')  # 
