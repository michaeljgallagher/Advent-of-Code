with open('08.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    res = []
    for line in raw_data.split('\n'):
        left, right = line.split(' | ')
        res.append((left, right))
    return res


data = parse_input(raw_data)

MAP = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


def part_one(data):
    res = 0
    for _, right in data:
        res += sum(len(x) in MAP for x in right.split())
    return res


def decode(line):
    left, right = line
    key = {
        MAP[len(signal)]: set(signal)
        for signal in left.split() + right.split()
        if len(signal) in MAP
    }

    for pattern in left.split() + right.split():
        cur = set(pattern)
        if len(pattern) == 6:
            if len(cur - key[4]) == 2:
                key[9] = cur
            elif len(cur - key[1]) == 4:
                key[0] = cur
            else:
                key[6] = cur
        if len(pattern) == 5:
            if len(cur - key[1]) == 3:
                key[3] = cur
            elif len(cur - key[4]) == 2:
                key[5] = cur
            else:
                key[2] = cur
    return key


def signal_to_num(key):
    res = {}
    for k, v in key.items():
        nk = ''.join(sorted(v))
        res[nk] = k
    return res


def part_two(data):
    res = 0
    for line in data:
        _, right = line
        key = decode(line)
        convert = signal_to_num(key)
        cur = 0
        for pattern in right.split():
            sig = ''.join(sorted(pattern))
            cur = cur * 10 + convert[sig]
        res += cur
    return res


print(f'Part 1: {part_one(data)}')  # 512
print(f'Part 2: {part_two(data)}')  # 1091165
