from collections import defaultdict
import random
import networkx as nx

with open('15.txt') as data:
    data = list(map(int, data.read().strip().split(',')))

ops = {
        1: lambda x, y: x+y,
        2: lambda x, y: x*y,
        7: lambda x, y: 1 if x < y else 0,
        8: lambda x, y: 1 if x == y else 0
        }


def find_modes(cmd):
    mode1 = mode2 = mode3 = 0
    cmd, params = cmd % 100, cmd // 100
    mode1 = params % 10
    params //= 10
    mode2 = params % 10
    params //= 10
    mode3 = params % 10
    return cmd, mode1, mode2, mode3


def find_params(program, pointer, relative_bound, mode1, mode2, mode3):
    if mode1 == 1:
        p1 = program[pointer + 1]
    elif mode1 == 2:
        p1 = program[program[pointer + 1] + relative_bound]
    else:
        p1 = program[program[pointer + 1]]

    if mode2 == 1:
        p2 = program[pointer + 2]
    elif mode2 == 2:
        p2 = program[program[pointer + 2] + relative_bound]
    else:
        p2 = program[program[pointer + 2]]

    if mode3 == 2:
        p3 = program[pointer + 3] + relative_bound
    else:
        p3 = program[pointer + 3]

    return p1, p2, p3


def intcode(program, inp):
    pointer = 0
    output = int
    relative_bound = 0
    grid = defaultdict(str)
    coord = (0, 0)
    directions = {1: (0, 1),
                  2: (0, -1),
                  3: (-1, 0),
                  4: (1, 0)}
    response = {0: '#',
                1: '.',
                2: '!'}
    grid[coord] = 'o'

    while True:
        try:
            cmd = program[pointer]
            mode1 = mode2 = mode3 = 0
            p1 = p2 = p3 = 0

            if cmd == 99:
                return output

            if cmd > 100:
                cmd, mode1, mode2, mode3 = find_modes(cmd)

            if cmd in [1, 2, 5, 6, 7, 8]:
                p1, p2, p3 = find_params(program, pointer, relative_bound, mode1, mode2, mode3)

                if cmd in [1, 2, 7, 8]:
                    program[p3] = ops[cmd](p1, p2)
                    pointer += 4

                elif cmd == 5:
                    pointer = p2 if p1 else pointer+3

                elif cmd == 6:
                    pointer = pointer+3 if p1 else p2

            elif cmd == 3:
                inp = random.choice(range(1, 5))
                new_coord = (coord[0]+directions[inp][0], coord[1]+directions[inp][1])
                if mode1 == 2:
                    program[program[pointer + 1] + relative_bound] = inp
                else:
                    program[program[pointer+1]] = inp
                pointer += 2

            elif cmd == 4:
                if mode1 == 1:
                    index = pointer + 1
                elif mode1 == 2:
                    index = program[pointer + 1] + relative_bound
                else:
                    index = program[pointer + 1]
                output = program[index]
                grid[new_coord] = response[output]
                if output:
                    coord = new_coord
                if output == 2:
                    return grid
                pointer += 2

            elif cmd == 9:
                if mode1 == 1:
                    index = pointer + 1
                elif mode1 == 2:
                    index = program[pointer + 1] + relative_bound
                else:
                    index = program[pointer + 1]
                relative_bound += program[index]
                pointer += 2

            else:
                return -1  # error

        except IndexError:
            oob_index = max(program[pointer + 1], p3)
            program += [0]*(oob_index - len(program)+1)


def display(grid):
    max_x = max(x for x, y in grid.keys())
    min_x = min(x for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())
    min_y = min(y for x, y in grid.keys())
    offset_x, offset_y = 0, 0
    if min_x < 0:
        offset_x = abs(min_x)
    if min_y < 0:
        offset_y = abs(min_y)
    screen = [[' ' for _ in range(max_x+offset_x+1)] for _ in range(max_y+offset_y+1)]
    for coord, val in grid.items():
        x = coord[0]
        y = coord[1]
        screen[y+offset_y][x+offset_x] = val
    screen[offset_y][offset_x] = 'O'
    for line in screen:
        print(''.join(line))


def make_graph(grid):
    G = nx.Graph()
    valid = set()
    for k, v in grid.items():
        if v == '.' or v == 'O':
            valid.add(k)
        if v == '!':
            oxygen = k
            valid.add(k)
    for x1, y1 in valid:
        for x2, y2 in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            i, j = (x1 + x2, y1 + y2)
            if (i, j) in valid:
                G.add_edge((x1, y1), (i, j))
    return G, oxygen


# Part 1
grid = intcode(data[:], 0)
display(grid)
G, oxygen = make_graph(grid)
print(f'Part 1: {nx.shortest_path_length(G, (0, 0), oxygen)}')  # 214

# Part 2
print(nx.eccentricity(G, v=oxygen))  # 344
