from itertools import product
from math import prod

with open("03.txt", "r") as file:
    data = file.read().strip()

SCHEMATIC = data.split("\n")
N, M = len(SCHEMATIC), len(SCHEMATIC[0])


def locate_symbols(symbols):
    return [
        (i, j)
        for i, row in enumerate(SCHEMATIC)
        for j, c in enumerate(row)
        if c in symbols
    ]


def find_num(i, j):
    l = r = j
    while 0 <= l and SCHEMATIC[i][l].isdigit():
        l -= 1
    while r < M and SCHEMATIC[i][r].isdigit():
        r += 1
    return l + 1, r


def solve(symbols, pt2=False):
    positions = locate_symbols(symbols)
    res = 0
    seen = set()
    for i, j in positions:
        cur = []
        for di, dj in filter(any, product([-1, 0, 1], repeat=2)):
            ni, nj = i + di, j + dj
            if (
                (ni, nj) not in seen
                and 0 <= ni < N
                and 0 <= nj < M
                and SCHEMATIC[ni][nj].isdigit()
            ):
                l, r = find_num(ni, nj)
                seen |= {(ni, q) for q in range(l, r + 1)}
                cur.append(int(SCHEMATIC[ni][l:r]))
        if pt2 and len(cur) == 2:
            res += prod(cur)
        elif not pt2:
            res += sum(cur)
    return res


print(f"Part 1: {solve('#$%&*+-/=@')}")  # 529618
print(f"Part 2: {solve('*', pt2=True)}")  # 77509019
