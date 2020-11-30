from itertools import permutations

with open('07.txt') as data:
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


def intcode(program, inputs, pointer=0):  # take in a list of inputs and last pointer
    while True:
        cmd = program[pointer]
        mode1 = mode2 = mode3 = 0

        if cmd == 99:
            return program[:], None, pointer  # function will now return this tuple for recallability

        if cmd > 100:
            cmd, mode1, mode2, mode3 = find_modes(cmd)

        if cmd in [1, 2, 5, 6, 7, 8]:
            p1 = program[pointer + 1] if mode1 else program[program[pointer + 1]]
            p2 = program[pointer + 2] if mode2 else program[program[pointer + 2]]
            index = program[pointer + 3]  # parameter3, always in position mode (mode3 is redundant and unused)
            if cmd in [1, 2, 7, 8]:
                program[index] = ops[cmd](p1, p2)
                pointer += 4
            elif cmd == 5:
                pointer = p2 if p1 else pointer+3
            elif cmd == 6:
                pointer = pointer+3 if p1 else p2

        elif cmd == 3:
            program[program[pointer+1]] = inputs.pop(0)
            pointer += 2

        elif cmd == 4:
            index = pointer+1 if mode1 else program[pointer+1]
            output = program[index]
            pointer += 2
            return program[:], output, pointer

        else:
            return -1  # error


# Part 1
max_signal = 0
for p in permutations(range(5)):
    nxt = 0
    for phase in p:
        nxt = intcode(data, [phase, nxt], 0)[1]
    max_signal = max(max_signal, nxt)
print(max_signal)  # 24625

# Part 2
max_signal = 0
for p in permutations(range(5, 10)):
    pointers = [0] * len(p)
    inputs = [[p[i]] for i in range(len(p))]
    inputs[0].append(0)
    output = 0
    amps = [data[:] for _ in range(len(p))]
    flag = True
    while flag:
        for i in range(len(p)):
            amps[i], new_output, pointer = intcode(amps[i], inputs[i], pointers[i])
            if not new_output:
                if output > max_signal:
                    max_signal = output
                flag = False
                break
            output = new_output
            pointers[i] = pointer
            inputs[(i+1) % len(inputs)].append(output)
print(max_signal)  # 36497698
