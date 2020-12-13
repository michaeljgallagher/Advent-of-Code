from functools import reduce

with open('13.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    return [int(x) if x.isdigit() else x for x in data.split(',')]


def part_one(data):
    time = 1002460
    buses = [x for x in data if type(x) is int]
    res = [(x - time % x, x) for x in buses]
    return reduce(lambda x, y: x*y, min(res))


def ext_gcd(a, b):
    if b == 1:
        return b
    initial_b = b
    x, y = 0, 1
    while a > 1:
        q = a//b
        a, b = b, a%b
        x, y = y - (q*x), x
    return y + initial_b if y<0 else y 


def chinese_remainder(nums, mods):
    product = reduce(lambda x, y: x*y, nums)
    total = 0
    for n, m in zip(nums, mods):
        p = product // n
        total += ext_gcd(p, n) * p * m
    return total % product


def part_two(data):
    buses = [x for x in data if type(x) is int]
    mods = [-i%v for i, v in enumerate(data) if v!='x']
    return chinese_remainder(buses, mods)


def part_two_sieve(data):
    '''
    Alternative solution that still utilizes the Chinese remainder theorem,
    but finds the answer by sieving
    '''
    buses = [x for x in data if type(x) is int]
    mods = [-i%v for i, v in enumerate(data) if v!='x']
    x, step = 0, 1
    for d, r  in zip(buses, mods):
        while x % d != r:
            x += step
        step *= d
    return x


data = parse_input(data)
print(f'Part 1: {part_one(data)}')  # 4808
print(f'Part 2: {part_two(data)}')  # 741745043105674
print(f'Part 2 (sieve): {part_two_sieve(data)}')  # 741745043105674
