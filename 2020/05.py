def convert(boarding_pass):
    return int(boarding_pass.translate(str.maketrans('FBLR', '0101')), 2)


def part_one(seats):
    return max(seats)


def part_two(seats):
    return list((set(range(min(seats), max(seats))) - seats))[0]


if __name__ == '__main__':
    with open('05.txt', 'r') as file:
        seats = set(convert(boarding_pass) for boarding_pass in file.read().split('\n'))
    
    print(f'Part 1: {part_one(seats)}')  # 959
    print(f'Part 2: {part_two(seats)}')  # 527
