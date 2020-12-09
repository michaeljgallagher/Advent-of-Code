with open('09.txt', 'r') as file:
    data = file.read()

def parse_input(data):
    return list(map(int, data.split('\n')))


def part_one(data):
    preamble = set(data[:25])
    i = 0
    while True:
        cur = data[i+25]
        if not any((cur - x) in preamble for x in preamble):
            return cur
        preamble.remove(data[i])
        preamble.add(data[i+25])
        i += 1

        
def part_two(data):
    cur, target = 0, 552655238
    i, j = 0, 0
    while j < len(data):
        while cur > target and i < j:
            cur -= data[i]
            i += 1
        if cur == target:
            return min(data[i:j]) + max(data[i:j])
        if j < len(data):
            cur += data[j]
        j += 1


data = parse_input(data)
print(f'Part 1: {part_one(data)}')  # 552655238
print(f'Part 2: {part_two(data)}')  # 70672245
