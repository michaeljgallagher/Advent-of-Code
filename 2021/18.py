from itertools import permutations

with open('18.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    return [eval(line) for line in raw_data.split('\n')]


DATA = parse_input(raw_data)
print(DATA)


def add_left(a, b):
    if not b:
        return a
    if type(a) == int:
        return a + b
    return [add_left(a[0], b), a[1]]


def add_right(a, b):
    if not b:
        return a
    if type(a) == int:
        return a + b
    return [a[0], add_right(a[1], b)]


def explode_pair(x, layer):
    if type(x) == int:
        return False, x, 0, 0
    left, right = x
    if layer == 4:
        return True, 0, left, right
    exploded, nxt, l, r = explode_pair(left, layer+1)
    if exploded:
        return True, [nxt, add_left(right, r)], l, 0
    exploded, nxt, l, r = explode_pair(right, layer+1)
    if exploded:
        return True, [add_right(left, l), nxt], 0, r
    return False, x, 0, 0


def split_num(x):
    if type(x) == int:
        if x > 9:
            return [x // 2, x // 2 + (x & 1)]
        return x
    l, r = x
    left = split_num(l)
    if left != l:
        return [left, r]
    return [l, split_num(r)]


def add_snails(a, b):
    res = [a, b]
    while True:
        exploded, res, _, _ = explode_pair(res, 0)
        if not exploded:
            prev = res
            res = split_num(res)
            if res == prev:
                return res


def magnitude(x):
    if type(x) == int:
        return x
    return 3 * magnitude(x[0]) + 2 * magnitude(x[1])


# print(add_snails([[[[4,3],4],4],[7,[[8,4],9]]], [1,1]))
# print(magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]))


def part_one():
    cur = DATA[0]
    for line in DATA[1:]:
        cur = add_snails(cur, line)
    return magnitude(cur)


def part_two():
    res = 0
    for a, b in permutations(DATA, 2):
        cur = add_snails(a, b)
        res = max(res, magnitude(cur))
    return res


print(f'Part 1: {part_one()}')  # 3647
print(f'Part 2: {part_two()}')  # 4600
