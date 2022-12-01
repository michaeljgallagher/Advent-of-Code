from collections import deque

INPUT = 349


def spinlock(n, steps):
    buffer = deque([0])
    for i in range(1, steps + 1):
        buffer.rotate(-n)
        buffer.append(i)
    return buffer


def part_one():
    buffer = spinlock(INPUT, 2017)
    return buffer[0]


def part_two():
    buffer = spinlock(INPUT, 50000000)
    return buffer[buffer.index(0) + 1]


print(f"Part 1: {part_one()}")  # 640
print(f"Part 2: {part_two()}")  # 47949463
