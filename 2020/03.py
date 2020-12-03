from collections import deque


with open('03.txt', 'r') as file:
    data = file.read().split('\n')


def part1(data, r, d):
    n = len(data)
    m = len(data[0])
    j = 0
    res = 0
    for i in range(0, n, d):
        cur = deque(data[i])
        cur.rotate(-j)
        if cur[0] == '#':
            res += 1
        j += r
    return res



def part2(data):
    res = 1
    for r, d in [(1,1), (3,1), (5, 1), (7, 1), (1, 2)]:
        res *= part1(data, r, d)
    return res


print(f'Answer for part 1: {part1(data, 3, 1)}')  # 270
print(f'Answer for part 2: {part2(data)}')  # 2122848000
