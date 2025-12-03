from functools import reduce


def parse_input():
    with open("03.txt", "r") as f:
        data = f.read()
    return [[int(x) for x in line] for line in data.splitlines()]


def solve(k):
    def max_joltage(bank, k):
        n = len(bank)
        drops = n - k
        stack = []
        for b in bank:
            while stack and drops > 0 and stack[-1] < b:
                stack.pop()
                drops -= 1
            stack.append(b)
        return reduce(lambda acc, x: acc * 10 + x, stack[:k])

    return sum(max_joltage(bank, k) for bank in parse_input())


print(f"Part 1: {solve(2)}")
print(f"Part 2: {solve(12)}")
