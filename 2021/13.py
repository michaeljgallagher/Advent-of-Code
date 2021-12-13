with open('13.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    a, b = raw_data.split('\n\n')
    nums = []
    for row in a.split('\n'):
        nums.append(tuple(map(int, row.split(','))))
    folds = []
    for row in b.split("\n"):
        x, y = row[11:].split('=')
        folds.append((x, int(y)))
    return nums, folds


POINTS, FOLDS = parse_input(raw_data)


def make_fold(axis, line, points):
    res = set()
    if axis == 'x':
        for x, y in points:
            if x > line:
                nx = 2 * line - x
                res.add((nx, y))
            else:
                res.add((x, y))
    else:
        for x, y in points:
            if y > line:
                ny = 2 * line - y
                res.add((x, ny))
            else:
                res.add((x, y))
    return res


def part_one():
    axis, line = FOLDS[0]
    points = set(POINTS)
    res = make_fold(axis, line, points)
    return len(res)


def part_two():
    points = set(POINTS)
    for fold in FOLDS:
        axis, line = fold
        points = make_fold(axis, line, points)
    X = max(x for x, _ in points)
    Y = max(y for _, y in points)
    grid = [[' ' for _ in range(X+1)] for _ in range(Y+1)]
    for j, i in points:
        grid[i][j] = '#'
    for row in grid:
        print(''.join(row))


print(f"Part 1: {part_one()}")  # 701
print(f"Part 2: {part_two()}")  # FPEKBEJL
