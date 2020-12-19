with open('19.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    rules_raw = [line for line in data.split('\n')[:135]]
    rules = {}
    for line in rules_raw:
        n, options = line.split(': ')
        n = int(n)
        if options in ('"a"', '"b"'):
            rules[n] = options[1]
        else:
            rules[n] = [[int(x) for x in option.split()] for option in options.split("|")]
    messages = [line for line in data.split('\n')[136:]]
    return rules, messages


rules, messages = parse_input(data)


def recur(rules, n, cur):
    if type(rules[n]) is str:
        return set([1]) if (cur and cur[0] == rules[n]) else set()

    res = set()
    for options in rules[n]:
        matches = set([0])
        for option in options:
            update = set()
            for x in matches:
                update |= {x+y for y in recur(rules, option, cur[x:])}
            matches = update
        res |= matches
    return res


def part_one(rules, messages):
    return sum(1 if len(message) in recur(rules, 0, message) else 0 for message in messages)


def part_two(rules, messages):
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    return sum(1 if len(message) in recur(rules, 0, message) else 0 for message in messages)


print(f'Part 1: {part_one(rules, messages)}')  # 239
print(f'Part 2: {part_two(rules, messages)}')  # 405
