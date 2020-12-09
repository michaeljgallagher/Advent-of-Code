with open('09.txt', 'r') as file:
    data = file.read()

def parse_input(data):
    return list(map(int, data.split('\n')))


def part_one(data):
    i = 0
    while True:
        found = False
        cur = set(data[i:i+25])
        target = data[i+25]
        for x in data[i:i+25]:
            if target - x in cur:
                i += 1
                found = True
        if not found:
            return target
        

def part_two(data):
    cur = data[0]
    i = 0
    j = 1
    while j <= len(data):
        while cur > 552655238 and i < j:
            cur -= data[i]
            i += 1
        if cur == 552655238:
            return min(data[i:j]) + max(data[i:j])
        if j < len(data):
            cur += data[j]
        j += 1


data = parse_input(data)

print(f'Part 1: {part_one(data)}')  # 552655238
print(f'Part 2: {part_two(data)}')  # 70672245
