with open('25.txt', 'r') as file:
    data = file.read()


def parse_data(data):
    return [int(x) for x in data.split('\n')]


key1, key2 = parse_data(data)


def find_loop_size(key):
    res = 0
    cur = 1
    while cur != key:
        cur = (cur * 7) % 20201227
        res += 1
    return res


def transform(key, loop_size):
    cur = 1
    for _ in range(loop_size):
        cur = (cur * key) % 20201227
    return cur


def part_one(key1, key2):
    return transform(key2, find_loop_size(key1))


print(f'Part 1: {part_one(key1, key2)}')  # 10548634
