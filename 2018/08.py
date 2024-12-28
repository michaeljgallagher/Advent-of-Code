from collections import deque


def parse_input():
    with open("08.txt", "r") as file:
        data = file.read()
    return deque(map(int, data.split(" ")))


def part_one():
    license = parse_input()

    def dfs():
        res = 0
        children, entries = license.popleft(), license.popleft()
        for _ in range(children):
            res += dfs()
        for _ in range(entries):
            res += license.popleft()
        return res

    return dfs()


def part_two():
    license = parse_input()

    def dfs():
        res = 0
        values = []
        children, entries = license.popleft(), license.popleft()
        for _ in range(children):
            values.append(dfs())
        for _ in range(entries):
            cur = license.popleft()
            if children == 0:
                res += cur
            elif 0 < cur <= children:
                res += values[cur - 1]
        return res

    return dfs()


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
