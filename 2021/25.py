with open('25.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    return [list(line) for line in raw_data.split('\n')]


DATA = parse_input(raw_data)


def move_east(arr):
    N, M = len(arr), len(arr[0])
    moves = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '>' and arr[i][(j+1) % M] == '.':
                moves.append((i, j, (j+1) % M))
    for i, j, nj in moves:
        arr[i][j] = '.'
        arr[i][nj] = '>'
    return arr, bool(moves)


def move_south(arr):
    N, M = len(arr), len(arr[0])
    moves = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'v' and arr[(i+1) % N][j] == '.':
                moves.append((i, (i+1) % N, j))
    for i, ni, j in moves:
        arr[i][j] = '.'
        arr[ni][j] = 'v'
    return arr, bool(moves)


def part_one(graph):
    res = 0
    moved = True
    while moved:
        graph, east = move_east(graph)
        graph, south = move_south(graph)
        moved = east or south
        res += 1
    return res


print(f'Part 1: {part_one(DATA)}')  # 458
