with open('10.txt', 'r') as data:
    data = data.read().split('\n')


def asteroid_locations(data):
    locations = []
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == '#':
                locations.append((x, y))
    return locations


def in_line(p1, p2, p3):
    return p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1]) == 0


def is_between(p1, p2, p3):
    '''
    check if point3 is between point1 and point2
    '''
    return p1 <= p3 <= p2 or p2 <= p3 <= p1


def is_blocked(p1, p2, p3):
    '''
    check if point3 is blocked by point2
    '''
    return in_line(p1, p2, p3) and is_between(p1, p3, p2)


def best_location(locations):
    best = [0]
    for p1 in locations:
        count = 0
        for p2 in locations:
            visible = True
            for p3 in locations:
                if p1 == p2 or p1 == p3 or p2 == p3:
                    continue
                if is_blocked(p1, p2, p3):
                    visible = False
                    break
            if visible:
                count += 1
        if count > best[0]:
            best = [count-1, p1]
    return best


locations = asteroid_locations(data)
print(best_location(locations))
