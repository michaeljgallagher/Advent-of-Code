from functools import cache


def parse_input(test=False):
    with open("11.txt", "r") as f:
        data = f.read()
    return {u: vs.split() for u, vs in (line.split(": ") for line in data.splitlines())}


G = parse_input()


@cache
def dfs(u, dac=False, fft=False):
    if u == "out":
        return int(dac and fft)
    dac |= u == "dac"
    fft |= u == "fft"
    return sum(dfs(v, dac, fft) for v in G[u])


def part_one():
    return dfs("you", True, True)


def part_two():
    return dfs("svr")


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
