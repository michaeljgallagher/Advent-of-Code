with open('11.txt', 'r') as file:
    data = file.read()

def parse_input(data):
    return [list(line) for line in data.split('\n')]


def check_seat(seat_pos, cur_seating):
    x, y = seat_pos
    count = 0
    for dx, dy in [(1,0), (1,1), (0,1), (-1,0), (-1,1), (0,-1), (-1,-1), (1,-1)]:
        if x+dx not in range(len(cur_seating)) or y+dy not in range(len(cur_seating[0])):
            continue
        if cur_seating[x+dx][y+dy] == '#':
            count += 1
    return count


def part_one(cur_seating):
    res = 0
    while True:
        occupy = set()
        deoccupy = set()
        for i in range(len(cur_seating)):
            for j in range(len(cur_seating[0])):
                if cur_seating[i][j] == 'L' and check_seat((i, j), cur_seating) == 0:
                    occupy.add((i, j))
                if cur_seating[i][j] == '#' and check_seat((i, j), cur_seating) >= 4:
                    deoccupy.add((i, j))
        if not occupy and not deoccupy:
            break
        for x, y in occupy:
            cur_seating[x][y] = '#'
        for x, y in deoccupy:
            cur_seating[x][y] = 'L'
        res += (len(occupy) - len(deoccupy))
    return res


def check_seat_2(seat_pos, cur_seating):
    x, y = seat_pos
    count = 0
    for dx, dy in [(1,0), (1,1), (0,1), (-1,0), (-1,1), (0,-1), (-1,-1), (1,-1)]:
        cur_x, cur_y = x+dx, y+dy
        while cur_x in range(len(cur_seating)) and cur_y in range(len(cur_seating[0])) and cur_seating[cur_x][cur_y] == '.':
            cur_x += dx
            cur_y += dy
        if cur_x not in range(len(cur_seating)) or cur_y not in range(len(cur_seating[0])):
            continue
        if cur_seating[cur_x][cur_y] == '#':
            count += 1
    return count


def part_two(cur_seating):
    res = 0
    while True:
        occupy = set()
        deoccupy = set()
        for i in range(len(cur_seating)):
            for j in range(len(cur_seating[0])):
                if cur_seating[i][j] == 'L' and check_seat_2((i, j), cur_seating) == 0:
                    occupy.add((i, j))
                if cur_seating[i][j] == '#' and check_seat_2((i, j), cur_seating) >= 5:
                    deoccupy.add((i, j))
        if not occupy and not deoccupy:
            break
        for x, y in occupy:
            cur_seating[x][y] = '#'
        for x, y in deoccupy:
            cur_seating[x][y] = 'L'
        res += (len(occupy) - len(deoccupy))
    return res


data = parse_input(data)
# print(f'Part 1: {part_one(data)}')  # 2472
print(f'Part 2: {part_two(data)}')  # 2197
