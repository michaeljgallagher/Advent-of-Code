from copy import deepcopy
from bootcode import BootCode

with open('08.txt', 'r') as file:
    data = file.read()

def parse_input(data):
    return [[line.split(' ')[0], int(line.split(' ')[1])] for line in data.split('\n')]


def part_one(data):
    bc = BootCode(data)
    bc.run()
    return bc.accum


def part_two(data):
    swap = {'jmp': 'nop', 'nop': 'jmp'}
    for i, v in enumerate(data):
        copy = deepcopy(data)
        if v[0] in ('jmp', 'nop'):
            copy[i][0] = swap[v[0]]
            bc = BootCode(copy)
            bc.run()
            if bc.idx >= bc.length:
                return bc.accum


data = parse_input(data)

print(f'Part 1: {part_one(data)}')  # 1859
print(f'Part 2: {part_two(data)}')  # 1235
