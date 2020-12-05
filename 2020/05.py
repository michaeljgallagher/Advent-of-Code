with open('05.txt', 'r') as file:
    data = file.read().split('\n')


def convert(boarding_pass):
    table = boarding_pass.maketrans('FBLR', '0101')
    return int(boarding_pass.translate(table), 2)


def find_seats(data):
    return set(convert(boarding_pass) for boarding_pass in data)


def part_one(seats):
    return max(seats)


def part_two(seats):
    lb, ub = min(seats), max(seats)
    return list((set(range(lb, ub)) - seats))[0]


if __name__ == '__main__':
    seats = find_seats(data)
    print(f'Part 1: {part_one(seats)}')  # 959
    print(f'Part 2: {part_two(seats)}')  # 527
