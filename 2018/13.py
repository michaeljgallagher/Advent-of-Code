def parse_input():
    with open("13.txt", "r") as file:
        data = file.read()
    a = set()
    b = set()
    intersection = set()
    carts = []
    for i, row in enumerate(data.splitlines()):
        for j, v in enumerate(row):
            if v == "\\":
                a.add((i, j))
            elif v == "/":
                b.add((i, j))
            elif v == "+":
                intersection.add((i, j))
            elif v == "^":
                carts.append((i, j, -1, 0, 0))
            elif v == "v":
                carts.append((i, j, 1, 0, 0))
            elif v == "<":
                carts.append((i, j, 0, -1, 0))
            elif v == ">":
                carts.append((i, j, 0, 1, 0))
    return a, b, intersection, carts


def solve(pt2=False):
    a, b, intersection, carts = parse_input()
    carts = [(i, j, di, dj, x, id) for id, (i, j, di, dj, x) in enumerate(carts)]
    pos = {(i, j): id for i, j, _, _, _, id in carts}
    crashed = set()
    while True:
        ncarts = []
        for i, j, di, dj, x, id in sorted(carts):
            if id in crashed:
                continue
            del pos[(i, j)]
            ni, nj = i + di, j + dj
            if (ni, nj) in pos:
                if not pt2:
                    return f"{nj},{ni}"
                crashed.add(pos[(ni, nj)])
                crashed.add(id)
                del pos[(ni, nj)]
                continue
            pos[(ni, nj)] = id
            if (ni, nj) in a:
                di, dj = dj, di
            elif (ni, nj) in b:
                di, dj = -dj, -di
            elif (ni, nj) in intersection:
                if x == 0:
                    di, dj = -dj, di
                elif x == 2:
                    di, dj = dj, -di
                x = (x + 1) % 3
            ncarts.append((ni, nj, di, dj, x, id))
        if len(ncarts) == 1:
            i, j, _, _, _, _ = ncarts.pop()
            return f"{j},{i}"
        carts = ncarts


def part_one():
    return solve()


def part_two():
    return solve(True)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
