with open('08.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    res = []
    for line in raw_data.split('\n'):
        left, right = line.split(' | ')
        res.append((left, right))
    return res


MAP = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

data = parse_input(raw_data)


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
    for signal in left.split() + right.split():
        length = len(signal)
        cur = set(signal)
        if length == 6:
            if len(cur - key[4]) == 2:
                key[9] = cur
            elif len(cur - key[1]) == 4:
                key[0] = cur
            else:
                key[6] = cur
        if length == 5:
            if len(cur - key[1]) == 3:
                key[3] = cur
            elif len(cur - key[4]) == 2:
                key[5] = cur
            else:
                key[2] = cur
    return key


def rev_key(key):
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
        rk = rev_key(key)
        cur = 0
        for signal in right.split():
            sig = ''.join(sorted(signal))
            cur = cur * 10 + rk[sig]
        res += cur
    return res


print(f'Part 1: {part_one(data)}')  # 512
print(f'Part 2: {part_two(data)}')  # 1091165
