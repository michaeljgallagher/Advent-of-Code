with open('02.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    res = []
    for line in raw_data.split('\n'):
        command, num = line.split()
        res.append((command, int(num)))
    return res


data = parse_input(raw_data)


def part_one(data):
    x = y = 0
    for command, num in data:
        if command == 'forward':
            x += num
        elif command == 'down':
            y += num
        else:
            y -= num
    return x * y


def part_two(data):
    x = y = aim = 0
    for command, num in data:
        if command == 'forward':
            x += num
            y += aim * num
        elif command == 'down':
            aim += num
        else:
            aim -= num
    return x * y


print(f'Part 1: {part_one(data)}')  # 1804520
print(f'Part 2: {part_two(data)}')  # 1971095320
