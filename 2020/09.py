with open('09.txt', 'r') as file:
    data = list(map(int, file.read().split('\n')))

def parse_input(data):
    list(map(int, file.read().split('\n')))


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
    i, j = 0, 1
    for i, v in enumerate(data):
        res = v
        n = 1
        while res < 552655238:
            res += data[i + n]
            n += 1
        if res ==552655238:
            return min(data[i:i+n]) + max(data[i:i+n])
#print(data)

print(f'Part 1: {part_one(data)}')  # 552655238
print(f'Part 2: {part_two(data)}')  # 70672245
