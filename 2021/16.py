from functools import reduce

with open('16.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    return ''.join(format(int(x, 16), '04b') for x in raw_data)


DATA = parse_input(raw_data)
VERSIONS = []


def parse_literal(s, i):
    ni = i
    res = []
    while s[ni] == '1':
        res.append(s[ni + 1 : ni + 5])
        ni += 5
    res.append(s[ni + 1 : ni + 5])
    ni += 5
    return ni, int(''.join(res), 2)


def parse_packet(s, i):
    version, tid = int(s[i : i + 3], 2), int(s[i + 3 : i + 6], 2)
    VERSIONS.append(version)
    if tid == 4:
        ni, val = parse_literal(s, i + 6)
        return ni, val

    values = []
    ltid = s[i + 6]
    val = 0
    if ltid == '0':
        total_len = int(s[i + 7 : i + 22], 2)
        ni = i + 22
        while ni < i + 22 + total_len:
            ni, val = parse_packet(s, ni)
            values.append(val)
    else:  # ltid == '1'
        packets = int(s[i + 7 : i + 18], 2)
        ni = i + 18
        for _ in range(packets):
            ni, val = parse_packet(s, ni)
            values.append(val)

    if tid == 0:
        val = sum(values)
    elif tid == 1:
        val = reduce(lambda x, y: x * y, values)
    elif tid == 2:
        val = min(values)
    elif tid == 3:
        val = max(values)
    elif tid == 5:
        val = int(values[0] > values[1])
    elif tid == 6:
        val = int(values[0] < values[1])
    elif tid == 7:
        val = int(values[0] == values[1])

    return ni, val


def part_one():
    _ = parse_packet(DATA, 0)
    return sum(VERSIONS)


def part_two():
    return parse_packet(DATA, 0)[1]


print(f'Part 1: {part_one()}')  # 955
print(f'Part 2: {part_two()}')  # 158135423448
