'''
<x=-3, y=10, z=-1>
<x=-12, y=-10, z=-5>
<x=-9, y=0, z=10>
<x=7, y=-5, z=-3>
'''

from itertools import combinations

io = [[-3, 10, 11], [0, 0, 0]]
europa = [[-12, -10, -5], [0, 0, 0]]
ganymede = [[-9, 0, 10], [0, 0, 0]]
callisto = [[7, -5, -3], [0, 0, 0]]


def gravity(moon1, moon2):
    for i in range(3):
        if moon1[0][i] < moon2[0][i]:
            moon1[1][i] += 1
            moon2[1][i] -= 1
        if moon1[0][i] > moon2[0][i]:
            moon1[1][i] -= 1
            moon2[1][i] += 1


def apply_velocity(moon):
    for i in range(3):
        moon[0][i] += moon[1][i]


def time_step():
    moons = [io, europa, ganymede, callisto]
    for moon1, moon2 in combinations(moons, 2):
        gravity(moon1, moon2)
    for moon in moons:
        apply_velocity(moon)


def total_energy(moon):
    pe = sum([abs(x) for x in moon[0]])
    ke = sum([abs(x) for x in moon[1]])
    return pe * ke


# Part 1
for i in range(1000):
    time_step()
print(sum([total_energy(moon) for moon in [io, europa, ganymede, callisto]]))  # 8310
