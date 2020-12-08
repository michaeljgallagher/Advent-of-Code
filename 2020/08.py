with open('08.txt', 'r') as file:
    data = file.read()

def parse_input(data):
    d = data.split('\n')
    res = [line.split(' ') for line in d]
    for i, v in enumerate(res):
        res[i] = [v[0], int(v[1])]
    return res


def part_one(data):
    seen = set()
    res, idx = 0, 0
    while idx < len(data) and idx not in seen:
        seen.add(idx)
        op, val = data[idx]
        if op == 'jmp':
            idx += val
        elif op == 'acc':
            res += val
            idx += 1
        else:
            idx += 1
    return res, idx


from copy import deepcopy
def part_two(data):
    for i, v in enumerate(data):
        copy = deepcopy(data)
        if v[0] in ('jmp', 'nop'):
            copy[i][0] = 'jmp' if v[0] == 'nop' else 'nop'
            res, idx = part_one(copy)
            if idx >= len(copy):
                return res





data = parse_input(data)

print(f'Part 1: {part_one(data)[0]}')  # 1859
print(f'Part 2: {part_two(data)}')  # 1235
