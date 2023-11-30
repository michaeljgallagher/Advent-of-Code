import re
from collections import defaultdict
from functools import cache
from itertools import product

with open("16.txt", "r") as file:
    data = file.read().strip()


def parse_input(data):
    valves, flows, g = set(), dict(), defaultdict(lambda: 1000)
    for v, f, us in re.findall(r"Valve (\w+) .*=(\d*); .* valves? (.*)", data):
        valves.add(v)
        if f != "0":
            flows[v] = int(f)
        for u in us.split(", "):
            g[u, v] = 1
    for k, i, j in product(valves, valves, valves):
        g[i, j] = min(g[i, j], g[i, k] + g[k, j])
    return valves, flows, g


VALVES, FLOWS, G = parse_input(data)


@cache
def search(t=30, u="AA", vs=frozenset(FLOWS), e=False):
    return max(
        [
            FLOWS[v] * (t - G[u, v] - 1) + search(t - G[u, v] - 1, v, vs - {v}, e)
            for v in vs
            if G[u, v] < t
        ]
        + [search(26, vs=vs) if e else 0]
    )


print(f"Part 1: {search()}")  # 1871
print(f"Part 2: {search(26, e=True)}")  # 2416
