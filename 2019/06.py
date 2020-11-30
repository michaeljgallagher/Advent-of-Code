with open('06.txt', 'r') as data:
    data = [x.split(')') for x in data.read().split('\n')]
data = data[:-1]
orbits = {x[1]: x[0] for x in data}


# PART 1

def count_paths(orbits):
    total = 0
    for planet in orbits.keys():
        curr = orbits[planet]
        while True:
            total += 1
            if curr == 'COM':
                break
            curr = orbits[curr]
    return total


print(count_paths(orbits))  # 142497


# PART 2

def find_path(origin, orbits):
    curr = orbits[origin]
    planets = []
    while True:
        if curr == 'COM':
            break
        planets.append(curr)
        curr = orbits[curr]
    return planets


def find_intersection(path1, path2):
    for x in path2:
        if x in path1:
            i = path1.index(x)
            k = path2.index(x)
            intersect = path1[:i] + path2[k:0:-1]
            break
    return intersect


my_path = find_path('YOU', orbits)
santa_path = find_path('SAN', orbits)
print(len(find_intersection(my_path, santa_path)))  # 301
