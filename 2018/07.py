import heapq
import re
from collections import defaultdict
from itertools import batched


def parse_input():
    with open("07.txt", "r") as file:
        data = file.read()
    edges = list(batched(re.findall(r" (\w) ", data), 2))
    indegs = defaultdict(int)
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        indegs[u]
        indegs[v] += 1
    return g, indegs


def solve(pt2=False):
    g, indegs = parse_input()
    heap = [u for u, indeg in indegs.items() if indeg == 0]
    heapq.heapify(heap)
    seen = set(heap)
    res = []
    workers = []
    t = 0
    while heap or workers:
        if pt2:
            while heap and len(workers) < 5:
                cur = heapq.heappop(heap)
                heapq.heappush(workers, (t + ord(cur) - ord("A") + 61, cur))
            t, cur = heapq.heappop(workers)
        else:
            cur = heapq.heappop(heap)
            res.append(cur)
        for nei in g[cur]:
            if nei in seen:
                continue
            indegs[nei] -= 1
            if indegs[nei] == 0:
                seen.add(nei)
                heapq.heappush(heap, nei)
    return t if pt2 else "".join(res)


def part_one():
    return solve()


def part_two():
    return solve(True)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
