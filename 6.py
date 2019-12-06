with open('6.txt', 'r') as data:
    data = [x.split(')') for x in data.read().split('\n')]
data = data[:-1]
orbits = {x[1]: x[0] for x in data}

total = 0
for planet in orbits.keys():
    curr = orbits[planet]
    while True:
        total += 1
        if curr == 'COM':
            break
        if curr in orbits.keys():
            curr = orbits[curr]

print(total)
