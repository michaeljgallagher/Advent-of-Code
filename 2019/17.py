with open('17.txt') as data:
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


def intcode(program, instructions=[0]):
    pointer = 0
    output = int
    relative_bound = 0
    outs = ''
    outputs = []
    insts = instructions

    while True:
        try:
            cmd = program[pointer]
            mode1 = mode2 = mode3 = 0
            p1 = p2 = p3 = 0

            if cmd == 99:
                return outputs, output

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
                inp = insts.pop(0)
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
                if output == 10:
                    outputs.append(outs)
                    outs = ''
                else:
                    outs += chr(output)
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


def find_intersections(grid):
    intersections = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            one, two, thr, fou = 0, 0, 0, 0
            if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[i])-1:
                continue
            else:
                if grid[i][j] == '#':
                    one = grid[i+1][j] == '#'
                    two = grid[i-1][j] == '#'
                    thr = grid[i][j+1] == '#'
                    fou = grid[i][j-1] == '#'
                    if int(one) + int(two) + int(thr) + int(fou) >= 3:
                        intersections.append((j, i))
    return intersections


def part_one(intersections):
    res = 0
    for x in intersections:
        res += x[0] * x[1]
    return res


# Part 1
grid = intcode(data[:])[0]
grid.pop()  # delete blank string
ints = find_intersections(grid)
print(f'Part 1: {part_one(ints)}')  # 7780


# Part 2
'''
(L6 R8 R12 L6 L8) [L10 L8 R12] (L6 R8 R12 L6 L8) {L8 L10 L6 L6} [L10 L8 R12] {L8 L10 L6 L6} [L10 L8 R12] 
(L6 R8 R12 L6 L8) {L8 L10 L6 L6} [L10 L8 R12]

A = (L6 R8 R12 L6 L8)
B = [L10 L8 R12]
C = {L8 L10 L6 L6}
MAIN = A B A C B C B A C B
'''

instructions = 'A,B,A,C,B,C,B,A,C,B\nL,6,R,8,R,12,L,6,L,8\nL,10,L,8,R,12\nL,8,L,10,L,6,L,6\nn\n'
'''instructions = ['A', ',', 'B', ',', 'A', ',', 'C', ',', 'B', ',', 'C', ',', 'B', ',', 'A', ',', 'C', ',', 'B', '\n',
                'L', ',', '6', ',', 'R', ',', '8', ',', 'R', ',', '12', ',', 'L', ',', '6', ',', 'L', ',', '8', '\n',
                'L', ',', '10', ',', 'L', ',', '8', ',', 'R', ',', '12', '\n',
                'L', ',', '8', ',', 'L', ',', '10', ',', 'L', ',', '6', ',', 'L', ',', '6', '\n',
                'n', '\n']'''

ints = [65, 44, 66, 44, 65, 44, 67, 44, 66, 44, 67, 44, 66, 44, 65, 44, 67, 44, 66, 10,
        76, 44, 54, 44, 82, 44, 56, 44, 82, 44, 49, 50, 44, 76, 44, 54, 44, 76, 44, 56, 10,
        76, 44, 49, 48, 44, 76, 44, 56, 44, 82, 44, 49, 50, 10,
        76, 44, 56, 44, 76, 44, 49, 48, 44, 76, 44, 54, 44, 76, 44, 54, 10,
        121, 10]
data2 = data[:]
data2[0] = 2
part2 = intcode(data2, ints)[1]
print(f'Part 2: {part2}')  # 1075882
