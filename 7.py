from intcode import Intcode
from itertools import permutations

with open('7.txt', 'r') as data:
    data = list(map(int, data.read().split(',')))

test = Intcode(data)
signals = []
for p in permutations(range(5)):
    output = 0
    for i in range(5):
        test.run(inputs=(p[i], output))
        output = test.output.pop()
    signals.append((output, p))
print(max(signals))  # (24625, (1, 3, 0, 4, 2))
