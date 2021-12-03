with open('03.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    return raw_data.split('\n')


data = parse_input(raw_data)


def part_one(data):
    transpose = [''.join(x) for x in zip(*data)]
    res = ['1' if x.count('1') > x.count('0') else '0' for x in transpose]
    gamma = int(''.join(res), 2)
    epsilon = gamma ^ (1 << len(res)) - 1
    return gamma * epsilon


def part_two(data):
    i = 0
    cur = data[:]
    while len(cur) > 1:
        col = [''.join(x) for x in zip(*cur)][i]
        keep = '1' if col.count('1') >= col.count('0') else '0'
        cur = [num for num in cur if num[i] == keep]
        i += 1
    oxygen_rating = int(cur[0], 2)

    i = 0
    cur = data[:]
    while len(cur) > 1:
        col = [''.join(x) for x in zip(*cur)][i]
        keep = '0' if col.count('1') >= col.count('0') else '1'
        cur = [num for num in cur if num[i] == keep]
        i += 1
    co2_rating = int(cur[0], 2)

    return oxygen_rating * co2_rating


print(f'Part 1: {part_one(data)}')  # 852500
print(f'Part 2: {part_two(data)}')  # 1007985
