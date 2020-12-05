with open('05.txt', 'r') as file:
    data = file.read().split('\n')


def find_row(boarding_pass):
    l, r = 0, 127
    for i in range(7):
            m = (l+r+1) // 2
            if boarding_pass[i] == 'F':
                r = m-1
            else:
                l = m
    return l


def find_col(boarding_pass):
    l, r = 0, 7
    for i in range(7, 10):
            m = (l+r+1) // 2
            if boarding_pass[i] == 'L':
                r = m-1
            else:
                l = m
    return l


def find_seats(data):
    seats = set()
    for boarding_pass in data:
        row = find_row(boarding_pass)
        col = find_col(boarding_pass)
        seats.add((row * 8) + col)
    return seats


def part_one(seats):
    return max(seats)


def part_two(seats):
    lb, ub = min(seats), max(seats)
    return list((set(range(lb, ub)) - seats))[0]


if __name__ == '__main__':
    seats = find_seats(data)
    print(f'Part 1: {part_one(seats)}')  # 959
    print(f'Part 2: {part_two(seats)}')  # 527
