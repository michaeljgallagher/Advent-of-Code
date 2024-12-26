def parse_input():
    with open("22.txt", "r") as file:
        data = file.read()
    grid = data.splitlines()
    return (
        {(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == "#"},
        len(grid) >> 1,
        len(grid[0]) >> 1,
    )


def part_one():
    infected, i, j = parse_input()
    di, dj = -1, 0
    res = 0
    for _ in range(10000):
        if (i, j) in infected:
            infected.remove((i, j))
            di, dj = dj, -di
        else:
            res += 1
            infected.add((i, j))
            di, dj = -dj, di
        i += di
        j += dj
    return res


def part_two():
    infected, i, j = parse_input()
    weakened = set()
    flagged = set()
    di, dj = -1, 0
    res = 0
    for _ in range(10000000):
        if (i, j) in infected:
            di, dj = dj, -di
            flagged.add((i, j))
            infected.remove((i, j))
        elif (i, j) in flagged:
            di, dj = -di, -dj
            flagged.remove((i, j))
        elif (i, j) in weakened:
            res += 1
            weakened.remove((i, j))
            infected.add((i, j))
        else:
            di, dj = -dj, di
            weakened.add((i, j))
        i += di
        j += dj
    return res


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
