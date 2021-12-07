with open('07.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    return list(map(int, raw_data.split(',')))


data = parse_input(raw_data)


def part_one(data):
    res = float('inf')
    for i in range(max(data)):
        res = min(res, sum(abs(x-i) for x in data))
    return res


def part_two(data):
    def gauss(n):
        return (n*(n+1))//2
    res = float('inf')
    for i in range(max(data)):
        res = min(res, sum(gauss(abs(x-i)) for x in data))
    return res


print(f'Part 1: {part_one(data)}')  # 335330
print(f'Part 2: {part_two(data)}')  # 92439766
