def load_data():
    with open('02.txt', 'r') as file:
        data = [x.split(' ') for x in file.read().split('\n')]
        for i in range(len(data)):
            cur = data[i][0]
            t = tuple(map(int, cur.split('-')))
            data[i][0] = t
            data[i][1] = data[i][1][0]
    return data


data = load_data()


def part1(data):
    res = 0
    for row in data:
        bounds, c, s = row
        a, b = bounds
        if a <= s.count(c) <= b:
            res += 1
    return res


def part2(data):
    res = 0
    for row in data:
        pos, c, s = row
        i, j = pos
        if (s[i-1] == c and s[j-1] != c) or (s[i-1] != c and s[j-1] == c):
            res += 1
    return res


print(f'Answer for part 1: {part1(data)}')  # 477
print(f'Answer for part 2: {part2(data)}')  # 686
