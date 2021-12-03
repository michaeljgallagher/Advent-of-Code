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
    def calc_rating(data, bit=1):
        i = 0
        cur = data[:]
        while len(cur) > 1:
            col = ''.join(list(zip(*cur))[i])
            keep = bit if col.count('1') >= col.count('0') else 1 - bit
            cur = [num for num in cur if num[i] == str(keep)]
            i += 1
        return int(cur[0], 2)

    oxygen_rating = calc_rating(data, 1)
    co2_rating = calc_rating(data, 0)

    return oxygen_rating * co2_rating


print(f'Part 1: {part_one(data)}')  # 852500
print(f'Part 2: {part_two(data)}')  # 1007985
