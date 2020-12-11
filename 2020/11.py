from collections import defaultdict

with open('11.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    return [list(line) for line in data.split('\n')]


def find_seats():
    seats = set()
    for i in range(N):
        for j in range(M):
            if GRID[i][j] == 'L':
                seats.add((i, j))
    return seats


GRID = parse_input(data)
N, M = len(GRID), len(GRID[0])
SEATS = find_seats()


def find_neighbors_one():
    res = defaultdict(list)
    for seat in SEATS:
        x, y = seat
        for dx, dy in [(1,0), (1,1), (0,1), (-1,0), (-1,1), (0,-1), (-1,-1), (1,-1)]:
            if (x+dx, y+dy) in SEATS:
                res[seat].append((x+dx, y+dy))
    return res


def check_seat(seat, occupied, neighbors):
    count = 0
    for neighbor in neighbors[seat]:
        if neighbor in occupied:
            count += 1
    return count


def run_cycles(neighbors, allowed=4):
    occupied, empty = SEATS.copy(), set()
    while True:
        occupy, deoccupy = set(), set()
        for seat in empty:
            if check_seat(seat, occupied, neighbors) == 0:
                occupy.add(seat)
        for seat in occupied:
            if check_seat(seat, occupied, neighbors) >= allowed:
                deoccupy.add(seat)
        if not occupy and not deoccupy:
            break
        occupied = (occupied - deoccupy) | occupy
        empty = (empty - occupy) | deoccupy
    return len(occupied)


def find_neighbors_two():
    res = defaultdict(list)
    for seat in SEATS:
        x, y = seat
        for dx, dy in [(1,0), (1,1), (0,1), (-1,0), (-1,1), (0,-1), (-1,-1), (1,-1)]:
            cur_x, cur_y = x+dx, y+dy
            while 0 <= cur_x < N and 0 <= cur_y < M and GRID[cur_x][cur_y] == '.':
                cur_x += dx
                cur_y += dy
            if (cur_x, cur_y) in SEATS:
                res[seat].append((cur_x, cur_y))
    return res


def part_one():
    return run_cycles(find_neighbors_one(), 4)


def part_two():
    return run_cycles(find_neighbors_two(), 5)


print(f'Part 1: {part_one()}')  # 2472
print(f'Part 2: {part_two()}')  # 2197
