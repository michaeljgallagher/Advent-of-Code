import re
from collections import deque


def parse_input():
    with open("09.txt", "r") as file:
        data = file.read()
    return map(int, re.findall(r"\d+", data))


PLAYERS, LAST = parse_input()


def solve(last):
    scores = [0] * PLAYERS
    q = deque([0])
    for i in range(1, last + 1):
        if i % 23 == 0:
            player = (i - 1) % PLAYERS
            q.rotate(7)
            scores[player] += i + q.pop()
            q.rotate(-1)
        else:
            q.rotate(-1)
            q.append(i)
    return max(scores)


def part_one():
    return solve(LAST)


def part_two():
    return solve(LAST * 100)


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
