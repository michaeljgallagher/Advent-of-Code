with open('01.txt', 'r') as file:
    data = list(map(int, file.read().split('\n')))


def part1(data):
    seen = set()
    for v in data:
        if 2020-v in seen:
            return v * (2020-v)
        else:
            seen.add(v)


def part2(data):
    data.sort()
    n = len(data)
    for i in range(n - 2):
        l, r = i+1, n-1
        while l < r:
            a, b, c = data[i], data[l], data[r]
            cur = a+b+c
            if cur == 2020:
                return a * b * c
            if cur-2020 > 0:
                r -= 1
            else:
                l += 1


print(f'Answer for part 1: {part1(data)}')  # 1018944
print(f'Answer for part 2: {part2(data)}')  # 8446464


'''
You could also just use itertools.combinations, 
but where's the fun in that? ¯\_(ツ)_/¯
'''


from itertools import combinations


def part1_alternative(data):
    for a, b in combinations(data, 2):
        if a + b == 2020:
            return a * b


def part2_alternative(data):
    for a, b, c in combinations(data, 3):
        if a + b + c == 2020:
            return a * b * c


print(part1_alternative(data))
print(part2_alternative(data))