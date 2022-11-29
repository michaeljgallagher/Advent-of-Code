from collections import defaultdict, deque

with open("12.txt", "r") as file:
    data = file.read().strip()

GRAPH = defaultdict(list)
for line in data.split("\n"):
    u, neis = line.split(" <-> ")
    GRAPH[u].extend(v for v in neis.split(", "))


def bfs(g, start):
    seen = set()
    q = deque([start])
    while q:
        u = q.popleft()
        if u in seen:
            continue
        seen.add(u)
        q.extend(g[u])
    return seen


def part_two(g):
    seen = set()
    res = 0
    for u in g:
        if u in seen:
            continue
        seen |= bfs(g, u)
        res += 1
    return res


print(f"Part 1: {len(bfs(GRAPH, '0'))}")  # 152
print(f"Part 2: {part_two(GRAPH)}")  # 186
