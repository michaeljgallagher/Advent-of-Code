data = [12,1,16,3,11,0]

def brute_force(data, end=2020):
    i = len(data)
    seen = {v: k+1 for k, v in enumerate(data)}
    cur = data[-1]
    while i < end:
        if cur not in seen:
            seen[cur] = i
            cur = 0
        else:
            prev = cur
            cur = i - seen[prev]
            seen[prev] = i
        i += 1
    return cur


def part_one(data):
    return brute_force(data, 2020)


def part_two(data):
    return brute_force(data, 30000000)


print(f'Part 1: {part_one(data)}')  # 1696
print(f'Part 2: {part_two(data)}')  # 37385
