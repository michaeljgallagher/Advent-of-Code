from itertools import combinations
import re
import numpy as np

with open('12.txt', 'r') as data:
    data = data.read().strip().split('\n')


def parse(data):
    regex = re.compile(r'<x=(.*), y=(.*), z=(.*)>')
    return [list(map(int, regex.findall(data[i])[0])) for i in range(len(data))]


def gravity(positions):
    new_positions = [[0 for _ in range(3)] for _ in range(4)]
    for i, j in combinations(range(4), 2):
        for k in range(3):
            if positions[i][k] < positions[j][k]:
                new_positions[i][k] += 1
                new_positions[j][k] -= 1
            if positions[i][k] > positions[j][k]:
                new_positions[i][k] -= 1
                new_positions[j][k] += 1
    return new_positions


def energy(positions, velocities):
    total = 0
    for i in range(4):
        total += sum([abs(x) for x in positions[i]]) * sum([abs(x) for x in velocities[i]])
    return total


def time_step(positions, velocities):
    d_v = gravity(positions)
    for i in range(4):
        for j in range(3):
            velocities[i][j] += d_v[i][j]
    for i in range(4):
        for j in range(3):
            positions[i][j] += velocities[i][j]


positions = parse(data)
velocities = [[0 for _ in range(3)] for _ in range(4)]
for _ in range(1000):
    time_step(positions, velocities)
print(energy(positions, velocities))  # 10944
