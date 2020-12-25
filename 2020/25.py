with open('25.txt', 'r') as file:
    data = file.read()


def parse_data(data):
    return [int(x) for x in data.split('\n')]


key1, key2 = parse_data(data)


def find_loop(key):
    res = 0
    cur = 1
    while cur != key:
        cur = (cur * 7) % 20201227
        res += 1
    return res


def transform(key, loop):
    cur = 1
    for _ in range(loop):
        cur = (cur * key) % 20201227
    return cur


def part_one(key1, key2):
    loop1, loop2 = find_loop(key1), find_loop(key2)
    return transform(key1, loop2)


print(f'Part 1: {part_one(key1, key2)}')  # 10548634
