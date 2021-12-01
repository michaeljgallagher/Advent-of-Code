with open('01.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    return list(map(int, raw_data.split('\n')))


data = parse_input(raw_data)


def compare(n, arr):
    return sum(arr[i] > arr[i - n] for i in range(n, len(arr)))


def part_one(data):
    return compare(1, data)


def part_two(data):
    return compare(3, data)


print(f'Part 1: {part_one(data)}')  # 1446
print(f'Part 2: {part_two(data)}')  # 1486
