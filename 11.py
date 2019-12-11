from collections import defaultdict

with open('11.txt') as data:
    data = list(map(int, data.read().split(',')))

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


def intcode(program, inp, pointer=0, relative_bound=0):
    outputs = []

    while True:
        try:
            cmd = program[pointer]
            mode1 = mode2 = mode3 = 0
            p1 = p2 = p3 = 0

            if cmd == 99:
                return None, None, None, None

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
                outputs.append(output)
                pointer += 2
                if len(outputs) == 2:
                    out = outputs.copy()
                    return program, out, pointer, relative_bound

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


def direction(curr, inst):
    if curr == 'U' or curr == 'D':
        if inst:
            return 'R' if curr == 'U' else 'L'
        else:
            return 'L' if curr == 'U' else 'R'
    else:
        if inst:
            return 'D' if curr == 'R' else 'U'
        else:
            return 'U' if curr == 'R' else 'D'


def step(point, dir):
    key = {'U': (0, 1),
           'D': (0, -1),
           'R': (1, 0),
           'L': (-1, 0)
           }
    return point[0] + key[dir][0], point[1] + key[dir][1]


def paint(curr, dir, instructions):
    if instructions[0] == 1:
        points_painted[curr] = '#'
    else:
        points_painted[curr] = '.'
    dir = direction(dir, instructions[1])
    curr = step(curr, dir)
    return curr, dir


def paint_points(data, curr, dir, color, pointer, relative_bound):
    while True:
        data, insts, pointer, relative_bound = intcode(data, color, pointer, relative_bound)
        if not insts:
            break
        curr, dir = paint(curr, dir, insts)
        if curr in points_painted.keys():
            if points_painted[curr] == '#':
                color = 1
            else:
                color = 0
        else:
            color = 0
    return points_painted


# Part 1
points_painted = defaultdict()
print(len(paint_points(data, (0,0), 'U', 0, 0, 0)))  # 1985


# Part 2
points_painted = defaultdict()
paint_points(data, (0,0), 'U', 1, 0, 0)

offset_x = min(points_painted.keys(), key=lambda x: x[0])[0] * -1
offset_y = min(points_painted.keys(), key=lambda x: x[1])[1] * -1
max_x = max(points_painted.keys(), key=lambda x: x[0])[0] + offset_x
max_y = max(points_painted.keys(), key=lambda x: x[1])[1] + offset_y
grid = [['.' for _ in range(max_x+1)] for _ in range(max_y+1)]
for point, color in points_painted.items():
    grid[point[1]+offset_y][point[0]+offset_x] = color
for row in reversed(grid):  # upside down
    print(''.join(row))  # BLCZCJLZ
