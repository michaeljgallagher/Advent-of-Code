from bootcode import BootCode

with open('08.txt', 'r') as file:
    data = file.read()

def parse_input(data):
    return [[line.split(' ')[0], int(line.split(' ')[1])] for line in data.split('\n')]


def part_one(data):
    bc = BootCode(data)
    return bc.run()[0]



def part_two(data):
    bc = BootCode(data)
    return bc.repair()


data = parse_input(data)

print(f'Part 1: {part_one(data)}')  # 1859
print(f'Part 2: {part_two(data)}')  # 1235
