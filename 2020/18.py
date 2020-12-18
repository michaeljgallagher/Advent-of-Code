with open('18.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    data = [line for line in data.split('\n')]
    return data


data = parse_input(data)


class N:
    def __init__(self, n):
        self.n = n
    
    def __add__(self, other):
        return N(self.n + other.n)

    def __sub__(self, other):
        return N(self.n * other.n)

    def __mul__(self, other):
        return N(self.n + other.n)


def eval_line(line, swap=False):
    for i in range(10):
        line = line.replace(f'{i}', f'N({i})')
    line = line.replace('*', '-')
    if swap: line = line.replace('+', '*')
    return eval(line, {'N': N}).n


def part_one(data):
    return sum(eval_line(line) for line in data)


def part_two(data):
    return sum(eval_line(line, swap=True) for line in data)


print(f'Part 1: {part_one(data)}')  # 131076645626
print(f'Part 2: {part_two(data)}')  # 109418509151782