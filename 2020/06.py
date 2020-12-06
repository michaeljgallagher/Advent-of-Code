from string import ascii_lowercase as letters

with open('06.txt', 'r') as file:
    data = file.read().split('\n\n')


def part_one(data):
    return sum(len(set(c for c in group if c !='\n')) for group in data)


def part_two(data):
    res = 0
    for group in data:
        cur = set(letters)
        for s in group.split():
            cur &= set(s)
        res += len(cur)
    return res


print(f'Part 1: {part_one(data)}')  # 6775
print(f'Part 2: {part_two(data)}')  # 3356
