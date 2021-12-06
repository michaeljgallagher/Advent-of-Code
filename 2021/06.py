with open('06.txt', 'r') as file:
    raw_data = file.read()


def parse_input(raw_data):
    res = [0] * 9
    for i in map(int, raw_data.split(',')):
        res[i] += 1
    return res


def solve(days):
    fish = parse_input(raw_data)
    for i in range(days):
        fish[(i + 7) % 9] += fish[i % 9]
    return sum(fish)


def part_one():
    return solve(80)


def part_two():
    return solve(256)


print(f'Part 1: {part_one()}')  # 391888
print(f'Part 2: {part_two()}')  # 1754597645339
