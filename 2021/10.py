with open("10.txt", "r") as file:
    raw_data = file.read()


def parse_input(raw_data):
    return raw_data.split("\n")


DATA = parse_input(raw_data)
MAP = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}
POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def corrupt_calc(line):
    stack = []
    res = 0
    for c in line:
        if not stack or c in "([{<":
            stack.append(c)
        else:
            cur = stack.pop()
            if MAP[c] != cur:
                res += POINTS[c]
    return res


def find_remaining_stack(line):
    stack = []
    for c in line:
        if not stack or c in "([{<":
            stack.append(c)
        elif MAP[c] == stack[-1]:
            stack.pop()
    return stack


def calc_score(stack):
    res = 0
    while stack:
        res *= 5
        res += POINTS[stack.pop()]
    return res


def part_one(data):
    return sum(corrupt_calc(line) for line in data)


def part_two(data):
    res = []
    for line in data:
        if not corrupt_calc(line):
            stack = find_remaining_stack(line)
            res.append(calc_score(stack))
    return sorted(res)[len(res) // 2]


print(f"Part 1: {part_one(DATA)}")  # 358737
print(f"Part 2: {part_two(DATA)}")  # 4329504793
