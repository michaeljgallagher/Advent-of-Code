from copy import deepcopy
from bootcode import BootCode
from tools import timer

with open('08.txt', 'r') as file:
    data = file.read()

def parse_input(data):
    return [[line.split(' ')[0], int(line.split(' ')[1])] for line in data.split('\n')]

@timer
def part_one(data):
    bc = BootCode(data)
    return bc.run()[0]


""" def part_two(data):
    swap = {'jmp': 'nop', 'nop': 'jmp'}
    for i, v in enumerate(data):
        copy = deepcopy(data)
        op, val = v
        if op in ('jmp', 'nop'):
            copy[i][0] = swap[op]
            bc = BootCode(copy)
            bc.run()
            if not bc.halt:
                return bc.accum """
@timer
def part_two(data):
    bc = BootCode(data)
    return bc.repair()


data = parse_input(data)

print(f'Part 1: {part_one(data)}')  # 1859
print(f'Part 2: {part_two(data)}')  # 1235
