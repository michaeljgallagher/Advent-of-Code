with open("07.txt", "r") as file:
    raw_data = file.read()


def parse_input(raw_data):
    return list(map(int, raw_data.split(",")))


def median(a):
    n = len(a)
    a.sort()
    if n & 1:
        return a[n // 2]
    else:
        return (a[n // 2 - 1] + a[n // 2]) / 2


def mean(a):
    return sum(a) / len(a)


def gauss(n):
    return (n * (n + 1)) // 2


def part_one(data):
    m = int(median(data))
    return sum(abs(x - m) for x in data)


def part_two(data):
    res = float("inf")
    m = int(mean(data))
    for i in range(m - 1, m + 2):
        res = min(res, sum(gauss(abs(x - i)) for x in data))
    return res


data = parse_input(raw_data)
print(f"Part 1: {part_one(data)}")  # 335330
print(f"Part 2: {part_two(data)}")  # 92439766
