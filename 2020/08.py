from copy import deepcopy
from bootcode import BootCode

with open('08.txt', 'r') as file:
    data = file.read()

def parse_input(data):
    return [[line.split(' ')[0], int(line.split(' ')[1])] for line in data.split('\n')]


'''def part_one(data):
    seen = set()
    res, idx = 0, 0
    while idx < len(data) and idx not in seen:
        seen.add(idx)
        op, val = data[idx]
        if op == 'jmp':
            idx += val - 1
        elif op == 'acc':
            res += val
        idx += 1
    return res, idx'''
def part_one(data):
    bc = BootCode(data)
    bc.run()
    return bc.accum


def part_two(data):
    for i, v in enumerate(data):
        copy = deepcopy(data)
        if v[0] in ('jmp', 'nop'):
            copy[i][0] = 'jmp' if v[0] == 'nop' else 'nop'
            res, idx = part_one(copy)
            if idx >= len(copy):
                return res


data = parse_input(data)

print(f'Part 1: {part_one(data)}')  # 1859
#print(f'Part 2: {part_two(data)}')  # 1235
