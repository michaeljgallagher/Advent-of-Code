'''
test1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
test2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']

test3 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
test4 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
'''


with open('3.txt', 'r') as file:
    data = file.readlines()
data1 = data[0].split(',')
data2 = data[1].split(',')


def make_wire(moves):
    point = [0, 0]
    wire = set()
    steps = 0
    step_count = {}
    for move in moves:
        direction = move[0]
        units = int(move[1:])
        if direction in ['R', 'U']:
            sign = 1
        else:
            sign = -1
        if direction in ['L', 'R']:
            axis = 0
        else:
            axis = 1
        for _ in range(units):
            point[axis] += sign
            new_point = tuple(point)
            wire.add(new_point)
            steps += 1
            if new_point not in step_count:
                step_count[new_point] = steps
    return wire, step_count


wire1 = make_wire(data1)
wire2 = make_wire(data2)
crosses = wire1[0].intersection(wire2[0])


mini = float('Inf')
for cross in crosses:
    mini = min(mini, abs(cross[0]) + abs(cross[1]))

print(mini)  # 273


cross_step_counts = [wire1[1][x] + wire2[1][x] for x in crosses]
print(min(cross_step_counts))  # 15622
