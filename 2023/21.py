from itertools import count, pairwise

with open("21.txt", "r") as file:
    data = file.read().strip()

G = data.split("\n")
START = next((i, j) for i, row in enumerate(G) for j, v in enumerate(row) if v == "S")
N, M = len(G), len(G[0])


def step(q, pt2=False):
    nq = set()
    for _ in range(len(q)):
        i, j = q.pop()
        for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if pt2 and G[ni % N][nj % M] != "#":
                nq.add((ni, nj))
            elif 0 <= ni < N and 0 <= nj < M and G[ni][nj] != "#":
                nq.add((ni, nj))
    return nq


def nth_term(seq, n):
    # https://www.radfordmathematics.com/algebra/sequences-series/difference-method-sequences/quadratic-sequences.html
    d1, d2 = (b - a for a, b in pairwise(seq))
    sd = d2 - d1
    x, y, z = sd, d1, seq[0]
    a = x >> 1
    b = y - (3 * a)
    c = z - b - a
    return (a * n * n) + (b * n) + c


def part_one():
    q = {START}
    for _ in range(64):
        q = step(q)
    return len(q)


def part_two():
    q = {START}
    seq = []
    for i in count(1):
        q = step(q, pt2=True)
        if i % N == 26501365 % N:
            seq.append(len(q))
            if len(seq) == 3:
                break
    return nth_term(seq, (26501365 // N) + 1)


print(f"Part 1: {part_one()}")  # 3722
print(f"Part 2: {part_two()}")  # 614864614526014
