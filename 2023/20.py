from collections import deque
from itertools import count
from math import lcm, prod

with open("20.txt", "r") as file:
    data = file.read().strip()

MODULES = [
    (a, b.split(", ")) for line in data.split("\n") for a, b in [line.split(" -> ")]
]


def initial_state(modules):
    ff, cj, g = {}, {}, {}
    for u, vs in modules:
        pfix, name = u[0], u[1:]
        if pfix == "%":
            g[name] = vs
            ff[name] = False
        elif pfix == "&":
            g[name] = vs
            cj[name] = {}
        else:  # broadcaster
            g[u] = vs
    for u, vs in g.items():
        for v in vs:
            if v in cj:
                cj[v][u] = False
    return ff, cj, g


def bfs(ff, cj, g, pt2=False, keys=None):
    res = [] if pt2 else [0, 0]
    for i in count(1):
        if not pt2 and i == 1001:
            return res
        q = deque([("_", "broadcaster", False)])
        while q:
            u, v, pulse = q.popleft()
            if not pt2:
                res[pulse] += 1
            if pt2 and not pulse and v in keys:
                res.append(i)
                if len(res) == len(keys):
                    return res
            if v in ff:
                if not pulse:
                    ff[v] = not ff[v]
                    npulse = ff[v]
                    for nv in g[v]:
                        q.append((v, nv, npulse))
            elif v in cj:
                cj[v][u] = pulse
                npulse = not all(cj[v].values())
                for nv in g[v]:
                    q.append((v, nv, npulse))
            elif v == "broadcaster":
                for nv in g[v]:
                    q.append((v, nv, pulse))


def part_one():
    ff, cj, g = initial_state(MODULES)
    return prod(bfs(ff, cj, g))


def part_two():
    # There's one machine that sends to 'rx'
    # Find that machine, then find the machines that send to it
    # We use these to determine distinct subgraphs with their own periods
    # See: https://i.redd.it/x6u0v3t9ee7c1.png
    # Another: https://i.redd.it/6kko113h8h7c1.png
    ff, cj, g = initial_state(MODULES)
    x = next(k for k, v in g.items() if "rx" in v)
    keys = [k for k, v in g.items() if x in v]
    return lcm(*bfs(ff, cj, g, True, keys))


print(f"Part 1: {part_one()}")  # 825896364
print(f"Part 2: {part_two()}")  # 243566897206981
