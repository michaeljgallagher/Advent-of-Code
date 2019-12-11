import math

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
#print(best_location(locations))  # [276, (17, 22)]


def find_angle(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    theta = math.degrees(math.atan2(y, x))
    if theta < 0:
        theta += 360
    theta += 90  # offset by 90
    theta %= 360
    return theta


def find_distance(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    return (x**2 + y**2)**.5


def append_angles(origin, locations):
    res = []
    angles = []
    for point in locations:
        if point == origin:
            continue
        angle = find_angle(origin, point)
        if angle in angles:
            angle += 360  # add 360 if angle repeats
        angles.append(angle)
        distance = find_distance(origin, point)
        res.append((point, angle, distance))
    return res


asteroids = append_angles((17, 22), locations)
asteroids.sort(key=lambda x: (x[1], x[2]))
print(asteroids[199])  # 200th hit; ((13, 21), 284.0362434679265, 4.123105625617661)
print(asteroids[199][0][0]*100 + asteroids[199][0][1])  # 1321
