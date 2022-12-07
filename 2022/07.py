from collections import defaultdict

with open("07.txt", "r") as file:
    data = file.read().strip()


def get_sizes(data):
    sizes = defaultdict(int)
    stack = []
    for line in data.split("\n"):
        cmd = line.split()
        if cmd[0] == "dir" or cmd[1] == "ls":
            continue
        if cmd[0].isdigit():
            cur = int(cmd[0])
            for i in range(1, len(stack) + 1):
                sizes[tuple(stack[:i])] += cur
        elif cmd[1:3] == ["cd", ".."]:
            stack.pop()
        else:
            stack.append(cmd[2])
    return sizes


SIZES = get_sizes(data)


def part_one():
    return sum(x for x in SIZES.values() if x <= 100000)


def part_two():
    need = 30000000 - (70000000 - SIZES[("/",)])
    res = SIZES[("/",)]
    for v in SIZES.values():
        if v >= need:
            res = min(res, v)
    return res


print(f"Part 1: {part_one()}")  # 1447046
print(f"Part 2: {part_two()}")  # 578710
