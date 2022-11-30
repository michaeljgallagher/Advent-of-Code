A, B = 679, 771
MOD = (1 << 31) - 1


def part_one(a, b):
    res = 0
    for _ in range(40000000):
        a = (a * 16807) % MOD
        b = (b * 48271) % MOD
        if a & 0xFFFF == b & 0xFFFF:
            res += 1
    return res


def part_two(a, b):
    def a_gen(x):
        while True:
            x = (x * 16807) % MOD
            if x % 4 == 0:
                yield x

    def b_gen(x):
        while True:
            x = (x * 48271) % MOD
            if x % 8 == 0:
                yield x

    na, nb = a_gen(a), b_gen(b)
    return sum(
        next(na) & 0xFFFF == next(nb) & 0xFFFF
        for _ in range(5000000)
    )


print(f"Part 1: {part_one(A, B)}")  # 626
print(f"Part 2: {part_two(A, B)}")  # 306
