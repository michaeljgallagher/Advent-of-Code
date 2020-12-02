with open('02.txt', 'r') as file:
    data = file.read().split('\n')


def part1(data):
    res = 0
    for row in data:
        bounds, c, s = row.split()
        a, b = map(int, bounds.split('-'))
        if a <= s.count(c[0]) <= b:
            res += 1
    return res


def part2(data):
    res = 0
    for row in data:
        pos, c, s = row.split()
        i, j = map(int, pos.split('-'))
        if (s[i-1] == c[0]) ^ (s[j-1] == c[0]):
            res += 1
    return res


print(f'Answer for part 1: {part1(data)}')  # 477
print(f'Answer for part 2: {part2(data)}')  # 686
