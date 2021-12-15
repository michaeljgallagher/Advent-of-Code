import heapq

with open('15.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    res = []
    for line in raw_data.split('\n'):
        res.append(list(map(int, line)))
    return res


CAVERN = parse_input(raw_data)
N, M = len(CAVERN), len(CAVERN[0])


def dijkstra(graph):
    r, c = len(graph), len(graph[0])
    costs = {}
    heap = [(0, 0, 0)]
    while heap:
        cost, i, j = heapq.heappop(heap)
        if (i, j) == (r - 1, c - 1):
            return cost
        for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= ni < r and 0 <= nj < c:
                ncost = cost + graph[ni][nj]
                if costs.get((ni, nj), float("inf")) <= ncost:
                    continue
                costs[(ni, nj)] = ncost
                heapq.heappush(heap, (ncost, ni, nj))


def part_one():
    return dijkstra(CAVERN)


def part_two():
    r, c = len(CAVERN) * 5, len(CAVERN[0]) * 5
    expanded = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            dist = i // N + j // M
            cur = CAVERN[i % N][j % M]
            cur = (cur + dist) % 9
            if cur == 0:
                cur = 9
            expanded[i][j] = cur
    return dijkstra(expanded)


print(f'Part 1: {part_one()}')  # 748
print(f'Part 2: {part_two()}')  # 3045
