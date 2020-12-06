with open('06.txt', 'r') as file:
    data = file.read().split('\n\n')


def part_one(data):
    return sum(len(set.union(*[set(list(s)) for s in group.split()])) for group in data)


def part_two(data):
    return sum(len(set.intersection(*[set(list(s)) for s in group.split()])) for group in data)


print(f'Part 1: {part_one(data)}')  # 6775
print(f'Part 2: {part_two(data)}')  # 3356
