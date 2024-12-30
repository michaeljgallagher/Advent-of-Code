def parse_input():
    with open("14.txt", "r") as file:
        data = file.read()
    return data.strip()


def part_one():
    a = [3, 7]
    i, j = 0, 1
    x = int(parse_input())
    while len(a) < x + 10:
        cur = a[i] + a[j]
        if cur > 9:
            a.append(1)
        a.append(cur % 10)
        i = (i + a[i] + 1) % len(a)
        j = (j + a[j] + 1) % len(a)
    return int("".join(map(str, a[x : x + 10])))


def part_two():
    a = [3, 7]
    i, j = 0, 1
    target = list(map(int, parse_input()))
    n = len(target)
    while True:
        cur = a[i] + a[j]
        if cur > 9:
            a.append(1)
            if len(a) >= n and a[-n:] == target:
                return len(a) - n
        a.append(cur % 10)
        if len(a) >= n and a[-n:] == target:
            return len(a) - n
        i = (i + a[i] + 1) % len(a)
        j = (j + a[j] + 1) % len(a)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
