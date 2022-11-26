from collections import deque

ELVES = 3012210


def part_one(n):
    # https://en.wikipedia.org/wiki/Josephus_problem
    return ((1 << (n.bit_length() - 1)) - 1 & n << 1) + 1


def part_two(n):
    left = deque(range(1, n >> 1))
    right = deque(range(n >> 1, n + 1))
    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.popleft()
        right.append(left.popleft())
        left.append(right.popleft())
    return left[0] or right[0]


print(f"Part 1: {part_one(ELVES)}")  # 1830117
print(f"Part 2: {part_two(ELVES)}")  # 1417887
