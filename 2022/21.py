from operator import add, floordiv, mul, sub


def parse_input():
    with open("21.txt", "r") as file:
        data = file.read()
    ops = {"+": add, "-": sub, "*": mul, "/": floordiv}
    monkeys = {}
    for line in data.splitlines():
        k, v = line.split(": ")
        if v.isdigit():
            monkeys[k] = int(v)
        else:
            monkeys[k] = (ops[v[5]], v[:4], v[-4:])
    return monkeys


def dfs(monkey, monkeys):
    if type(monkeys[monkey]) is int:
        return monkeys[monkey]
    op, a, b = monkeys[monkey]
    return op(dfs(a, monkeys), dfs(b, monkeys))


def part_one():
    monkeys = parse_input()
    return dfs("root", monkeys)


def part_two():
    monkeys = parse_input()
    a, b = monkeys["root"][1:]
    l, r = 0, dfs("root", monkeys)
    while l < r:
        m = l + (r - l >> 1)
        monkeys["humn"] = m
        if (x := dfs(a, monkeys)) == (y := dfs(b, monkeys)):
            return m
        if x > y:
            l = m + 1
        else:
            r = m


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
