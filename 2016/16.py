STATE = list(map(int, "11110010111001001"))


def dragon_curve(a, disk):
    while len(a) < disk:
        b = [1 - x for x in reversed(a)]
        a = a + [0] + b
    return a[:disk]


def checksum(a):
    while not len(a) & 1:
        a = [int(a[i] == a[i + 1]) for i in range(0, len(a), 2)]
    return "".join(map(str, a))


print(f"Part 1: {checksum(dragon_curve(STATE, 272))}")  # 01110011101111011
print(f"Part 2: {checksum(dragon_curve(STATE, 35651584))}")  # 11001111011000111
